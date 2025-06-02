# backend/aetherion/crypto.py
import os
from cryptography.fernet import Fernet

# In production, generate your key once and store in ENV (e.g. via `export VAULT_KEY=...`)
VAULT_KEY = os.environ.get("VAULT_KEY", None)
if VAULT_KEY is None:
    # For local testing only—generate a random key at startup.
    VAULT_KEY = Fernet.generate_key().decode()

fernet = Fernet(VAULT_KEY.encode())

def encrypt_file(raw_bytes: bytes) -> bytes:
    return fernet.encrypt(raw_bytes)

def decrypt_file(cipher_bytes: bytes) -> bytes:
    return fernet.decrypt(cipher_bytes)
