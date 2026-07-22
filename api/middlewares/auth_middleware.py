from flask import  request
from config.load_env import get_env
from werkzeug.exceptions import (
    Unauthorized,
)

def validate_token():
    env = get_env()
    TOKEN = env.getenv("AUTH_TOKEN")
    client_token = request.headers.get("Authorization")
    
    if client_token != TOKEN:
        raise Unauthorized("Auth Token Is Not Authorized")

