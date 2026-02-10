from backend.encryption import encrypt_data, decrypt_data
from backend.dos_protection import RateLimiter

limiter = RateLimiter(3, 30)

def handle_request(device_id, message):
    if not limiter.is_allowed(device_id):
        return False, "DoS protection triggered"

    encrypted = encrypt_data(message)
    decrypted = decrypt_data(encrypted)

    return True, {
        "encrypted": encrypted.decode(),
        "decrypted": decrypted
    }
