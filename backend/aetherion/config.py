# Aetherion/backend/aetherion/config.py

import os
import json

def load_config():
    # Try loading from config.json, fallback to environment variables
    try:
        with open("backend/config.json") as f:
            return json.load(f)
    except Exception:
        return {
            "SECRET_KEY": os.environ.get("SECRET_KEY", "aetherion-default-secret"),
            "SQLALCHEMY_DATABASE_URI": os.environ.get("DATABASE_URL", "sqlite:///aetherion.db"),
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "JWT_SECRET_KEY": os.environ.get("JWT_SECRET_KEY", "aetherion-jwt-secret"),
        }
