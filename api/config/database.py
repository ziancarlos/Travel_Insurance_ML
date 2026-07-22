from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


class Base(DeclarativeBase):
    pass


def create_database(env):
    DATABASE_URL = (
        f"postgresql+psycopg2://"
        f"{env.getenv('DB_USER')}:"
        f"{env.getenv('DB_PWD')}@"
        f"{env.getenv('DB_HOST')}:"
        f"{env.getenv('DB_PORT')}/"
        f"{env.getenv('DB_NAME')}"
    )

    engine = create_engine(
        DATABASE_URL,
        echo=True
    )

    SessionLocal = sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False
    )

    return engine, SessionLocal