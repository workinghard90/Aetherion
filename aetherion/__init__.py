# aetherion/__init__.py

from flask import Flask
from aetherion.config import get_config
from aetherion.extensions import db, migrate
from aetherion.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    db.init_app(app)
    migrate.init_app(app, db)
    register_routes(app)

    return app
