from cryptography.fernet import Fernet
import base64
import os

key = base64.urlsafe_b64encode(os.urandom(32))
fernet = Fernet(key)

def encrypt_file(data):
    return fernet.encrypt(data)

def decrypt_file(data):
    return fernet.decrypt(data)
