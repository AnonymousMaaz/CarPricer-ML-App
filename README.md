# CarPricer – Fueling Car Prices

Machine learning powered car price prediction web app built with **Django** and **scikit-learn**.

## Local development

Requires a trained model in `models/*.pkl` (the app loads the first `.pkl` it finds there).

```bash
python -m venv car_env
car_env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

## Render deployment (Django)

Render only needs:

- This repo pushed to GitHub
- `requirements.txt` in the root
- `Procfile` containing:

  ```text
  web: gunicorn car_pricer.wsgi
  ```

In Render:

1. Create **New Web Service** → **Build from GitHub**.
2. Select this repo.
3. Set **Build Command**: `pip install -r requirements.txt`.
4. Set **Start Command**: `gunicorn car_pricer.wsgi`.
5. Add environment variable `PYTHON_VERSION` matching your local version (e.g. `3.13.5`).

