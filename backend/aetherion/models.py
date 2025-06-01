# Aetherion/backend/aetherion/models.py

from .extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hashed_password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # (Any other fields you need, e.g. email, roles, etc.)


class VaultFile(db.Model):
    __tablename__ = "vault_files"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256), nullable=False)
    original_name = db.Column(db.String(256), nullable=False)
    mime_type = db.Column(db.String(80), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref=db.backref("files", lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "original_name": self.original_name,
            "mime_type": self.mime_type,
            "size": self.size,
            "user_id": self.user_id,
            "uploaded_at": self.uploaded_at.isoformat(),
        }
