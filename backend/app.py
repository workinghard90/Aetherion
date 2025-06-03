# backend/app.py

import os
from flask import Flask
from .config import Config
from .extensions import db, migrate, cors, jwt
from .routes import register_routes
from .health import bp as health_bp

# If you have an auth blueprint under backend/aetherion/auth.py, import it like this:
# from backend.aetherion.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    jwt.init_app(app)

    # Register the health-check blueprint
    app.register_blueprint(health_bp, url_prefix="/health")

    # If you actually want to enable the aetherion-auth blueprint, uncomment below:
    # app.register_blueprint(auth_bp, url_prefix="/aetherion/auth")

    # Register the main API routes
    register_routes(app)

    return app

app = create_app()
