from . import db

class Universe(db.Model):
    __tablename__ = "universe"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    properties = db.Column(db.JSON, nullable=True)  # store JSON data
    created_at = db.Column(db.DateTime, server_default=db.func.now())
