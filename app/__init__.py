from flask import Flask
from flask_migrate import Migrate
from .database import db
from .api.auth import auth_bp
from .api.vault import vault_bp
from .api.health import health_bp  # optional ping route

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(vault_bp, url_prefix="/vault")
    app.register_blueprint(health_bp)  # optional /ping

    return app
