# CarPricer — ML-Powered Car Price Estimator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=flat&logo=django&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=flat&logo=render&logoColor=white)

**Predict the resale price of any used car instantly using a Random Forest model trained on 8,000+ real listings.**

[Live Demo](https://carpricer-ml-app.onrender.com) · [Report Bug](https://github.com/AnonymousMaaz/CarPricer-ML-App/issues)

</div>

---

## What it does

Enter a few details about a used car — manufacturing year, kilometres driven, fuel type, seller type, transmission, and ownership history — and get an instant ML-based price estimate in rupees.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **ML Model** | Random Forest Regressor (scikit-learn 1.8) |
| **Backend** | Django 6.0 + Gunicorn 21.2 |
| **Preprocessing** | Custom pipeline (mileage, engine, power, torque extraction + categorical encoding + owner one-hot) |
| **Deployment** | Render (free tier) |
| **Dataset** | Car details (8,129 rows, Kaggle) |

---

## Model Performance

| Metric | Score |
|--------|-------|
| **R² (test set)** | 0.9920 |
| **Model type** | Random Forest — 300 estimators |
| **Training rows** | Full dataset (~8k after cleaning) |

---

## Input Features

| Feature | Values |
|---------|--------|
| Year | Manufacture year |
| Km Driven | Total kilometres driven |
| Fuel Type | Petrol / Diesel / CNG / LPG |
| Seller Type | Dealer / Individual / Trustmark Dealer |
| Transmission | Manual / Automatic |
| Owner History | First / Second / Third / Fourth & Above / Test Drive |

---

## Local Setup

```bash
# 1. Clone
git clone https://github.com/AnonymousMaaz/CarPricer-ML-App.git
cd CarPricer-ML-App

# 2. Create and activate virtual environment
python -m venv env
env\Scripts\activate        # Windows
# source env/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Place your trained model
# Copy your random_forest_model.pkl into the models/ folder

# 5. Run migrations and start
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`

---

## Project Structure

```
CarPricer-ML-App/
├── car_pricer/          # Django project (settings, urls, wsgi)
├── predictor/           # App — views, forms, services, templates
├── preprocess.py        # Feature engineering pipeline
├── Dataset/             # Training data (Car details.csv)
├── models/              # Trained .pkl model (not in repo — too large for GitHub)
├── requirements.txt
├── Procfile             # Render start command
└── render.yaml          # Render build config
```

---

## Deployment

Deployed on [Render](https://render.com) (free tier).  
The `.pkl` model file exceeds GitHub's 100 MB limit so it is hosted separately and downloaded at build time via `MODEL_URL` env var.

---

## License

MIT
