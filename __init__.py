import os
from flask import Flask
from aetherion.config import get_config
from aetherion.extensions import db, migrate, cors
from aetherion.api import register_blueprints

def create_app():
    app = Flask(__name__)
    config = get_config(os.getenv("FLASK_ENV", "development"))
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    register_blueprints(app)
    return app
