# Aetherion/backend/aetherion/health.py

from flask import Blueprint

health_bp = Blueprint("health", __name__)

@health_bp.route("/healthz", methods=["GET"])
def index():
    return {"status": "healthy"}, 200
