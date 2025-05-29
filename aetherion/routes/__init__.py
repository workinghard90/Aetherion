# aetherion/routes/__init__.py

from aetherion.routes.buttons import buttons_bp
from aetherion.api.auth import auth_bp
from aetherion.api.health import health_bp

def register_routes(app):
    app.register_blueprint(buttons_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(health_bp)
