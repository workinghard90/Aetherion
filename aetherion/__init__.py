from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from aetherion.extensions import db, migrate, cors
from aetherion.models import User, Document
from aetherion.routes import register_routes
from aetherion.api.auth import auth_bp
from aetherion.api.health import health_bp
from aetherion.admin.views import SecureAdmin

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    register_routes(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(health_bp)

    admin = Admin(app, index_view=SecureAdmin(), template_mode="bootstrap4")
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Document, db.session))

    return app
