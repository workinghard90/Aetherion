import os
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from aetherion.extensions import db, migrate, cors
from aetherion.models import User
from aetherion.routes import register_routes
from aetherion.admin.views import SecureAdmin
import aetherion.models as models
import inspect

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    # 🛡️ Fallback if SQLALCHEMY_DATABASE_URI is not set
    if not app.config.get("SQLALCHEMY_DATABASE_URI"):
        fallback_uri = "sqlite:///vault.db"
        print("⚠️  SQLALCHEMY_DATABASE_URI not set, falling back to:", fallback_uri)
        app.config["SQLALCHEMY_DATABASE_URI"] = fallback_uri

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    register_routes(app)

    admin = Admin(app, index_view=SecureAdmin(), template_mode="bootstrap4")
    for name, cls in vars(models).items():
        if inspect.isclass(cls) and hasattr(cls, "__tablename__"):
            admin.add_view(ModelView(cls, db.session))

    return app
