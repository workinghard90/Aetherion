# aetherion/routes.py

from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return jsonify({"message": "Aetherion API is running."})


def register_routes(app):
    app.register_blueprint(main_bp)
