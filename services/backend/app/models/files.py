# services/backend/app/models/file.py

from ..database import db

class VaultFile(db.Model):
    ...
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
