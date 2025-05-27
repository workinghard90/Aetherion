# services/backend/app/services/crypto.py

from cryptography.fernet import Fernet
import os

# Read or generate a persistent key (solo vault)
VAULT_KEY_PATH = ".vault_key"

def load_vault_key():
    if os.path.exists(VAULT_KEY_PATH):
        with open(VAULT_KEY_PATH, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(VAULT_KEY_PATH, "wb") as f:
            f.write(key)
        return key

fernet = Fernet(load_vault_key())

def encrypt_file(file_data: bytes) -> bytes:
    return fernet.encrypt(file_data)

def decrypt_file(file_data: bytes) -> bytes:
    return fernet.decrypt(file_data)
