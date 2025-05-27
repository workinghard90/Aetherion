from aetherion.extensions import db

class VaultFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    original_name = db.Column(db.String(120), nullable=False)
    mime_type = db.Column(db.String(120))
    size = db.Column(db.Integer)
    user_id = db.Column(db.Integer, nullable=False)
