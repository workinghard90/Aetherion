import os
import json

def load_config():
    try:
        with open("backend/config.json") as f:
            return json.load(f)
    except Exception:
        return {
            "SECRET_KEY": os.environ.get("SECRET_KEY", "default-secret"),
            "SQLALCHEMY_DATABASE_URI": os.environ.get("DATABASE_URL", "sqlite:///aetherion.db"),
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "JWT_SECRET_KEY": os.environ.get("JWT_SECRET_KEY", "jwt-secret")
        }
{
  "DEBUG": false,
  "SQLALCHEMY_DATABASE_URI": "sqlite:///universe.db",
  "SQLALCHEMY_TRACK_MODIFICATIONS": false,
  "UPLOAD_FOLDER": "uploads",
  "JWT_SECRET": "AUTUMN&CAELUM"
}
