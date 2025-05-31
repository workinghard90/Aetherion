from . import db

class VaultFile(db.Model):
    __tablename__ = "vault_files"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)        # encrypted file name on disk
    original_name = db.Column(db.String(255), nullable=False)   # user uploaded original name
    mime_type = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Integer, nullable=False)                # size of encrypted data
    user_id = db.Column(db.Integer, nullable=False)             # uploader’s user ID
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())
