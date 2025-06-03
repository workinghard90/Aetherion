# Aetherion/backend/app.py

from flask import Flask
from aetherion.auth import auth_bp
from aetherion.health import health_bp
from aetherion.vault import vault_bp
from aetherion.scrolls import scrolls_bp
from aetherion.oracle import oracle_bp
from aetherion.extensions import db, jwt, cors
from aetherion.config import load_config

def create_app():
    app = Flask(__name__)
    app_config = load_config()
    app.config.update(app_config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(health_bp, url_prefix="/health")
    app.register_blueprint(vault_bp, url_prefix="/vault")
    app.register_blueprint(scrolls_bp, url_prefix="/archive")
    app.register_blueprint(oracle_bp, url_prefix="/oracle")

    return app
