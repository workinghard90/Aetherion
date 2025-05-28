# === aetherion/config.py ===

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///aetherion.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
    JWT_SECRET = os.getenv("JWT_SECRET", "dev_secret")

def get_config():
    return Config
