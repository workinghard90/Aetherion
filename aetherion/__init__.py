# aetherion/__init__.py

from flask import Flask
from aetherion.extensions import db
from aetherion.config import get_config
from aetherion.api.auth import auth_bp
from aetherion.api.vault import vault_bp
from aetherion.api.health import health_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(vault_bp, url_prefix="/vault")
    app.register_blueprint(health_bp)

    return app
