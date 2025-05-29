from aetherion.extensions import db

class Button(db.Model):
    id = db.Column(db.String, primary_key=True)
    label = db.Column(db.String, nullable=False)
    sigil = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
