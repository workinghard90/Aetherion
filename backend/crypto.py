from cryptography.fernet import Fernet
import os

# In production, store this key securely (e.g. AWS Secrets Manager)
FERNET_KEY = os.getenv("FERNET_KEY") or Fernet.generate_key().decode()
fernet = Fernet(FERNET_KEY.encode())

def encrypt_file(data: bytes) -> bytes:
    return fernet.encrypt(data)

def decrypt_file(token: bytes) -> bytes:
    return fernet.decrypt(token)
