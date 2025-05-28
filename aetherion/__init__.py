from flask import Flask
from flask_cors import CORS
from aetherion.extensions import db
from aetherion.api.auth import auth_bp
from aetherion.api.vault import vault_bp
from aetherion.api.health import health_bp
from aetherion.config import get_config

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    db.init_app(app)
    CORS(app, origins=["https://aetherionai.netlify.app"])

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(vault_bp, url_prefix="/vault")
    app.register_blueprint(health_bp, url_prefix="/")

    return app
