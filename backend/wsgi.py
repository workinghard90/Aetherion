# backend/wsgi.py
# This is the entrypoint for Gunicorn on Render
from app import create_app

app = create_app()
