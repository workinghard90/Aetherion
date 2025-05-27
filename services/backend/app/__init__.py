# services/backend/app/__init__.py

import os
from flask import Flask
from dotenv import load_dotenv
from .database import db
from .api.vault import vault_bp
from .api.auth import auth_bp

load_dotenv()  # Load .env values into environment

def create_app():
    app = Flask(__name__)
    env = os.getenv("FLASK_ENV", "development")

    if env == "production":
        from config import ProductionConfig as AppConfig
    else:
        from config import DevelopmentConfig as AppConfig

    app.config.from_object(AppConfig)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(vault_bp, url_prefix="/vault")

    return app

from .models.audit import AuditLog
