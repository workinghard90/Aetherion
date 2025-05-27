# services/backend/app/__init__.py

from flask import Flask
from .database import db
from flask_migrate import Migrate

from .api.vault import vault_bp
from .api.auth import auth_bp
from .models.audit import AuditLog  # Ensure table is created

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(vault_bp, url_prefix="/vault")

    return app
