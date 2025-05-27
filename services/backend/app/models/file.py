# services/backend/app/models/file.py

from datetime import datetime
from ..database import db

class VaultFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    original_name = db.Column(db.String(255), nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    mime_type = db.Column(db.String(100))
    size = db.Column(db.Integer)

from datetime import datetime
from ..database import db

class VaultFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    original_name = db.Column(db.String(255), nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    mime_type = db.Column(db.String(100))
    size = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # New fields
    title = db.Column(db.String(255), nullable=True)
    tags = db.Column(db.String(255), nullable=True)  # comma-separated
