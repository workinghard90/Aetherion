import os

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET = os.getenv("JWT_SECRET", "super-secret")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")


def get_config():
    env = os.getenv("FLASK_ENV", "development")
    return BaseConfig
