import os
from dotenv import load_dotenv
import re

load_dotenv()

class Config:
    # 1) SECRET_KEY and JWT_SECRET_KEY come from environment, with your provided defaults.
    SECRET_KEY    = os.getenv("SECRET_KEY", "aetherion2025")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "AUTUMN&CAELUM")

    # 2) DATABASE_URL from environment; but if it looks like an HTTP URL (e.g. "https://…"), 
    #    we fall back to a local SQLite file to avoid SQLAlchemy dialect errors.
    raw_db_url = os.getenv("DATABASE_URL", "").strip()
    if raw_db_url and re.match(r"^[a-zA-Z]+://", raw_db_url) and not raw_db_url.startswith(("sqlite://", "postgresql://", "mysql://", "postgres://")):
        # If they set DATABASE_URL to something like "https://…" (which is invalid for SQLAlchemy),
        # default to a local file called aetherion.db
        SQLALCHEMY_DATABASE_URI = "sqlite:///aetherion.db"
    else:
        # Otherwise, use raw_db_url if provided, or fall back to SQLite.
        SQLALCHEMY_DATABASE_URI = raw_db_url or "sqlite:///aetherion.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
