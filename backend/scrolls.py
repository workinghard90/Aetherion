from flask import Blueprint, jsonify
from .models import Scroll

bp = Blueprint("scrolls", __name__)

@bp.route("/", methods=["GET"])
def get_all_scrolls():
    scrolls = Scroll.query.all()
    return jsonify([{"id": s.id, "title": s.title} for s in scrolls])
