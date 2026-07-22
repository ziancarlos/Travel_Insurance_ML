from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_env():
    load_dotenv();
    
    if os.getenv("APP_ENV") == "dev":
        load_dotenv(BASE_DIR / ".env.dev")
    else:
        load_dotenv(BASE_DIR / ".env.prod")
    
    return os