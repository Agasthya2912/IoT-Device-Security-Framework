from cryptography.fernet import Fernet
import hashlib

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(data):
    return cipher.encrypt(data.encode())

def decrypt_data(data):
    return cipher.decrypt(data).decode()

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()
