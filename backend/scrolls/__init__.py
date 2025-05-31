from flask import Blueprint
scrolls_bp = Blueprint("scrolls", __name__, url_prefix="/api/scrolls")

from .routes import *  # import route functions
