# backend/wsgi.py

from .app import create_app

# This “app” variable is discovered by Gunicorn when you run:
#    gunicorn backend.wsgi:app
app = create_app()
