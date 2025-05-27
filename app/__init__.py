import os
from flask import Flask
from flask_migrate import Migrate
from .database import db
from .api.auth import auth_bp
from .api.vault import vault_bp
from .api.health import health_bp  # /ping route

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    env = os.getenv("FLASK_ENV", "development").capitalize()
    app.config.from_object(f"config.{env}Config")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(vault_bp, url_prefix="/vault")
    app.register_blueprint(health_bp)

    return app
