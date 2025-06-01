# backend/config.py

import os

# Flask settings
DEBUG = True

# Secret key (you should override this in production via an env var)
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")

# SQLAlchemy / database URL.
# For local dev, we’ll use SQLite. In production you can set DATABASE_URL in env.
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL",
    "sqlite:///aetherion.db"
)

# Disable track modifications to suppress warnings
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Where uploaded files should be stored (ensure this folder is writable)
UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", "/tmp/uploads")
