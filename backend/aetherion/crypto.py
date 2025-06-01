# Aetherion/backend/aetherion/crypto.py

from cryptography.fernet import Fernet
import os

# Generate a key once and store it in an environment variable in production!
FERNET_KEY = os.getenv("FERNET_KEY", Fernet.generate_key().decode())
fernet = Fernet(FERNET_KEY.encode())

def encrypt_file(binary_data: bytes) -> bytes:
    return fernet.encrypt(binary_data)

def decrypt_file(token: bytes) -> bytes:
    return fernet.decrypt(token)
