from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/", methods=["GET"])
def check_health():
    return jsonify(status="Aetherion backend is online 🌌")
