# backend/config.py

import os

class Config:
    # If you set DATABASE_URL in Render's Environment Variables, it will override the default SQLite.
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///universe.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")

    # Where uploaded files will be stored. Ensure this folder is writable.
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", "/opt/render/project/data/uploads")
