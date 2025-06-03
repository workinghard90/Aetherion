# backend/app.py

import os
import logging
from logging.config import dictConfig
from flask import Flask, request, jsonify
from .config import Config
from .extensions import db, migrate, cors, jwt

# Import the blueprints (make sure these files exist exactly as named)
from .health import bp as health_bp        # Provides GET /health/
from .auth import bp as auth_bp            # Provides POST /auth/register and POST /auth/login
from .scrolls import bp as scrolls_bp      # Provides GET /scrolls
from .vault import bp as vault_bp          # Provides POST /vault/upload, GET /vault/download/<id>

# We still need to add an Oracle‐specific route below (no blueprint)
# because there is no separate blueprint file for oracle.


def create_app():
    # ─── 1. Set up logging so that the Render console will show Flask logs ───
    dictConfig({
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default"
            }
        },
        "root": {
            "level": "INFO",
            "handlers": ["wsgi"]
        }
    })

    # ─── 2. Create Flask app and load config ───
    app = Flask(__name__)
    app.config.from_object(Config)

    # ─── 3. Initialize extensions ───
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    jwt.init_app(app)

    # ─── 4. Register blueprints ───
    app.register_blueprint(health_bp, url_prefix="/health")
    app.register_blueprint(auth_bp,   url_prefix="/auth")
    app.register_blueprint(scrolls_bp, url_prefix="/scrolls")
    app.register_blueprint(vault_bp,   url_prefix="/vault")

    # ─── 5. Create “Oracle” route (since no separate blueprint file) ───
    from .oracle import OracleService

    @app.route("/oracle/insights", methods=["POST"])
    @jwt_required  # you must import jwt_required from auth_middleware
    def oracle_insights(user_id):
        """
        Expects JSON: { "prompt": "<your prompt string>" }
        Returns JSON from OracleService.get_insights(...)
        """
        data = request.get_json() or {}
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"msg": "Prompt is required"}), 400

        # Example: pass your actual Oracle endpoint via environment or default
        oracle_endpoint = os.getenv("ORACLE_ENDPOINT", "")
        if not oracle_endpoint:
            return jsonify({"msg": "Oracle endpoint not configured"}), 500

        oracle = OracleService(oracle_endpoint)
        result = oracle.get_insights(prompt)
        return jsonify(result), 200

    return app

# ─── 6. Instantiate the app ───
app = create_app()
