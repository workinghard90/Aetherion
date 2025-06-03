# backend/app.py

import os
from flask import Flask
from .config import Config
from .extensions import db, migrate, cors, jwt
from .routes import register_routes

# Import the health-check blueprint (bp) from health.py
from .health import bp as health_bp

# (Optionally, if you want to enable the Aetherion auth blueprint, use this:)
# from backend.aetherion.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    jwt.init_app(app)

    # Register the health-check blueprint under '/health'
    app.register_blueprint(health_bp, url_prefix="/health")

    # If you enabled auth_bp above, register it here:
    # app.register_blueprint(auth_bp, url_prefix="/aetherion/auth")

    # Register the main API routes
    register_routes(app)

    return app

# Create the Flask application instance
app = create_app()
