# hari-demo-web

A simple Flask demo web app.

## Stack
- Python 3.11
- Flask (dev), Gunicorn (production)

## Layout
- `app.py` — Flask application entrypoint
- `templates/index.html` — landing page
- `requirements.txt` — Python dependencies

## Running
The `Server` workflow runs `python app.py` on port 5000 (host `0.0.0.0`).

## Deployment
Configured as autoscale, serving via Gunicorn on port 5000.
