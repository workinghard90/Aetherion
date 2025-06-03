import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Production defaults (can be overridden via actual environment variables)
    SECRET_KEY = os.getenv("SECRET_KEY", "aetherion2025")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "https://aetherionai-mobile.onrender.com"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "AUTUMN&CAELUM")
