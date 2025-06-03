import os
from cryptography.fernet import Fernet

VAULT_KEY = os.environ.get("VAULT_KEY", Fernet.generate_key().decode())
fernet = Fernet(VAULT_KEY.encode())

def encrypt(data: bytes) -> bytes:
    return fernet.encrypt(data)

def decrypt(data: bytes) -> bytes:
    return fernet.decrypt(data)
