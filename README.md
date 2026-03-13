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

## Render deployment

**→ Full step-by-step guide: [RENDER_DEPLOY.md](RENDER_DEPLOY.md)** (env vars, secrets, model file, and service setup).

You need:

- This repo on GitHub (with `requirements.txt` and `Procfile`: `web: gunicorn car_pricer.wsgi`).
- On Render: set **Build Command** `pip install -r requirements.txt`, **Start Command** `gunicorn car_pricer.wsgi`, and the environment variables and model setup described in `RENDER_DEPLOY.md`.

