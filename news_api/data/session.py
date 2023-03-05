import logging
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from news_api.dependencies import get_settings

settings = get_settings()
engine = create_engine(settings.DATABASE_URL)#, pool_pre_ping=True, pool_size=10)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        logging.info("DB session created")
        yield db
    finally:
        logging.info("DB session CLOSED")
        db.close()
