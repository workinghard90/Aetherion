from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from aetherion.admin.views import SecureAdmin
from aetherion.extensions import db
from aetherion.models import User, Document  # Add your models

def create_app():
    app = Flask(__name__)
    # config, init_extensions, blueprints...

    admin = Admin(app, index_view=SecureAdmin(), template_mode="bootstrap4")
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Document, db.session))

    return app
