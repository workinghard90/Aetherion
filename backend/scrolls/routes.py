from . import scrolls_bp
from flask import jsonify

@scrolls_bp.route("/", methods=["GET"])
def list_scrolls():
    # Return a JSON list of “scroll” metadata (e.g. from a DB table)
    return jsonify([]), 200
