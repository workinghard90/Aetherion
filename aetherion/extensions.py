# aetherion/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
admin = Admin(name="Aetherion Admin", template_mode="bootstrap4")
