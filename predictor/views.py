import sys
from pathlib import Path

# Ensure project root is on sys.path so `preprocess` is importable
_root = str(Path(__file__).resolve().parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

from django.shortcuts import render

from .forms import CarInputForm
from .services import predict_selling_price


def predict_price(request):
    predicted_price = None
    error_message = None
    form = CarInputForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        try:
            predicted_price = predict_selling_price(form.cleaned_data)
        except FileNotFoundError as e:
            error_message = str(e)
        except Exception as e:
            error_message = (
                f"Prediction failed: {type(e).__name__}: {e}. "
                "Please check the model file and try again."
            )

    return render(
        request,
        "predictor/predict_form.html",
        {
            "form": form,
            "predicted_price": predicted_price,
            "error_message": error_message,
        },
    )
