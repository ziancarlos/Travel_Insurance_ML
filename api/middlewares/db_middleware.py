from flask import g
from config.database import create_database
from config.load_env import get_env
def create_db_session():
    env = get_env()
    _, SessionLocal = create_database(env)

    g.db = SessionLocal()


def close_db_session(exception=None):
    db = g.pop("db", None)

    if db:
        db.close()