import jwt
import datetime
import hashlib
from functools import wraps
from flask import request, abort

SECRET_KEY = "your_secret_key"
HASH_SECRET = "hash_secret_key"

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

def hash_username(username):
    return hashlib.sha256((username + HASH_SECRET).encode()).hexdigest()

def generate_token(username, role):
    payload = {
        "username": username,
        "role": role,
        "hash": hash_username(username),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            abort(403, "Token missing")
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            if data["hash"] != hash_username(data["username"]):
                abort(403, "Invalid token hash")
        except:
            abort(403, "Invalid or expired token")
        return f(*args, **kwargs)
    return decorated
