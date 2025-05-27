# services/backend/app/services/crypto.py

from cryptography.fernet import Fernet
import base64
import hashlib

# Deterministic secret for dev (must replace in prod)
KEY = hashlib.sha256(b"default_dev_key").digest()
FERNET_KEY = base64.urlsafe_b64encode(KEY[:32])
fernet = Fernet(FERNET_KEY)

def encrypt_file(data: bytes) -> bytes:
    return fernet.encrypt(data)

def decrypt_file(data: bytes) -> bytes:
    return fernet.decrypt(data)
