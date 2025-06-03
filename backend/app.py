# backend/app.py

import os
import logging
from logging.config import dictConfig
from flask import Flask, request, jsonify
from .config import Config
from .extensions import db, migrate, cors, jwt

from .health import bp as health_bp       # GET /health/
from .auth import bp as auth_bp           # POST /auth/register, POST /auth/login
from .scrolls import bp as scrolls_bp     # GET /scrolls/
from .vault import bp as vault_bp         # POST /vault/upload, GET /vault/download/<id>
from .auth_middleware import jwt_required # Decorator for JWT protection

def create_app():
    # ─── 1. Logging configuration ───
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

    # ─── 5. Root route ───
    @app.route("/", methods=["GET"])
    def index():
        return jsonify({"msg": "Welcome to the Aetherion API"}), 200

    # ─── 6. Oracle route ───
    from .oracle import OracleService

    @app.route("/oracle/insights", methods=["POST"])
    @jwt_required
    def oracle_insights(user_id):
        """
        Expects JSON: { "prompt": "<…>" }
        Returns the OpenAI Chat Completion result (JSON).
        """
        data = request.get_json() or {}
        prompt = data.get("prompt", "").strip()
        if not prompt:
            return jsonify({"msg": "Prompt is required"}), 400

        oracle = OracleService()
        result = oracle.get_insights(prompt)

        # If OracleService returns an "error" key, treat it as a 500
        if isinstance(result, dict) and "error" in result:
            return jsonify(result), 500

        return jsonify(result), 200

    return app

# ─── 7. Instantiate the app ───
app = create_app()
