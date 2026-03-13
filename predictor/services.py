from pathlib import Path
from typing import Any, Dict

import numpy as np
import pandas as pd
import pickle

from preprocess import CarDataPreprocessor

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

_model = None


def _load_model():
    """
    Lazily load the first available .pkl model from the models folder.
    This matches how models are saved in model_utils.save_model.
    """
    global _model
    if _model is not None:
        return _model

    if not MODELS_DIR.exists():
        raise FileNotFoundError(
            f"No 'models' folder found at {MODELS_DIR}. "
            "Train a model by running `python main.py` and saving it."
        )

    candidates = sorted(MODELS_DIR.glob("*.pkl"))
    if not candidates:
        raise FileNotFoundError(
            f"No .pkl model files found in {MODELS_DIR}. "
            "After training with `main.py`, save your model (e.g. 'my_model') "
            "so it appears as 'models/my_model.pkl'."
        )

    model_path = candidates[0]
    with model_path.open("rb") as f:
        _model = pickle.load(f)

    return _model


def _build_feature_row(cleaned_data: Dict[str, Any]) -> pd.DataFrame:
    """
    Build a single-row feature DataFrame that matches the training features.

    We:
    - Run the same preprocessing pipeline used during training on the full dataset.
    - Take the median feature values as a baseline.
    - Override selected features with user inputs.
    """
    dataset_path = BASE_DIR / "Dataset" / "Car details.csv"
    processor = CarDataPreprocessor(str(dataset_path))
    data = processor.process()

    # Recreate X exactly as in main.py
    X = data.drop(["selling_price", "name", "owner"], axis=1)

    # Start from median values to keep everything aligned with training distribution
    base_row = X.median(numeric_only=True)

    # Override with user-provided values where we have them
    # Column names are inferred from the original dataset.
    if "year" in base_row.index:
        base_row["year"] = cleaned_data["year"]

    if "km_driven" in base_row.index:
        base_row["km_driven"] = cleaned_data["kms_driven"]

    # Encode categorical features in the same way as in preprocess.encode_categorical
    fuel_raw = cleaned_data["fuel_type"]
    fuel_val = 1 if fuel_raw == "Petrol" else 0 if fuel_raw == "Diesel" else -1
    if "fuel" in base_row.index:
        base_row["fuel"] = fuel_val

    seller_raw = cleaned_data["seller_type"]
    if seller_raw == "Individual":
        seller_val = 1
    elif seller_raw == "Dealer":
        seller_val = 0
    else:
        seller_val = -1
    if "seller_type" in base_row.index:
        base_row["seller_type"] = seller_val

    transmission_raw = cleaned_data["transmission"]
    transmission_val = 1 if transmission_raw == "Manual" else 0
    if "transmission" in base_row.index:
        base_row["transmission"] = transmission_val

    # Handle owner one-hot columns (created in encode_owner)
    owner_value = cleaned_data["owner"]
    owner_categories = [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car",
    ]
    owner_cols = [c for c in X.columns if c in owner_categories]
    for col in owner_cols:
        base_row[col] = 1 if col == owner_value else 0

    # Return as a single-row DataFrame with columns in the original order
    return pd.DataFrame([base_row[c] for c in X.columns], index=X.columns).T


def predict_selling_price(cleaned_data: Dict[str, Any]) -> float:
    """
    Accepts validated form data and returns the predicted selling price.
    """
    model = _load_model()
    features = _build_feature_row(cleaned_data)

    prediction = model.predict(features)
    if isinstance(prediction, (list, np.ndarray)):
        prediction_value = float(prediction[0])
    else:
        prediction_value = float(prediction)

    return round(prediction_value, 2)

