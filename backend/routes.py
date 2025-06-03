from flask import Blueprint
from backend.auth import auth_bp
from backend.vault import vault_bp
from backend.oracle import oracle_bp
from backend.scrolls import scrolls_bp
from backend.health import health_bp

api_bp = Blueprint("api", __name__)
api_bp.register_blueprint(auth_bp, url_prefix="/auth")
api_bp.register_blueprint(vault_bp, url_prefix="/vault")
api_bp.register_blueprint(oracle_bp, url_prefix="/oracle")
api_bp.register_blueprint(scrolls_bp, url_prefix="/archive")
api_bp.register_blueprint(health_bp, url_prefix="/health")
