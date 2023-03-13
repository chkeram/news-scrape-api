import logging
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
import retrying


from news_api.dependencies import get_settings


settings = get_settings()
engine = create_engine(f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}")#, pool_pre_ping=True, pool_size=10)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        logging.info("DB session created")
        yield db
    finally:
        logging.info("DB session CLOSED")
        db.close()


@retrying.retry(wait_fixed=2000, stop_max_delay=10000, stop_max_attempt_number=4)
def check_postgres_connection():
    """
    Make sure DB is available on startup. Log errors if something is wrong
    :return:
    """

    conn = psycopg2.connect(
        host=settings.POSTGRES_HOST,
        port=5432,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        database=settings.POSTGRES_DB
    )
    conn.close()
