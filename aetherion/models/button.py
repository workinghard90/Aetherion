from datetime import datetime
from aetherion.extensions import db

class Button(db.Model):
    id = db.Column(db.String, primary_key=True)
    label = db.Column(db.String, nullable=False)
    sigil = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
