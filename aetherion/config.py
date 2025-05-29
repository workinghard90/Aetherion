import os

class BaseConfig:
    SECRET_KEY = os.getenv("JWT_SECRET", "aetherion_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///vault.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", 104857600))
    PROJECT_NAME = "Aetherion"

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    FLASK_ENV = "development"

class ProductionConfig(BaseConfig):
    DEBUG = False
    FLASK_ENV = "production"

def get_config():
    env = os.getenv("FLASK_ENV", "production").lower()
    return DevelopmentConfig if env == "development" else ProductionConfig
