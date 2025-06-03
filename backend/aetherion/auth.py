from flask import Blueprint, request, jsonify
from backend.aetherion.database import get_session  # if you need direct DB sessions
# (Or you can continue to use your main DB from .extensions if preferred)

auth_bp = Blueprint("aetherion_auth", __name__)

@auth_bp.route("/aetherion/hello", methods=["GET"])
def hello_aetherion():
    return jsonify({"msg": "Hello from Aetherion Auth Blueprint!"})
