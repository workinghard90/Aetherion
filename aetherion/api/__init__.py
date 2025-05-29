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

from .extensions import db, admin
from .models import Button

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    admin.init_app(app)

    with app.app_context():
        from .views import buttons_bp
        app.register_blueprint(buttons_bp)

        db.create_all()

        from flask_admin.contrib.sqla import ModelView
        admin.add_view(ModelView(Button, db.session))

    return app
