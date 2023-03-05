import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "news-api"
    PROJECT_VERSION = 1.0
    DOMAIN_ENV: str = "development"
    MOCK_API_CALLS_FOR_TESTS = False
    POSTGRES_USER = 'postgres'
    POSTGRES_PASSWORD = 'postgres'
    POSTGRES_DB = 'mydatabase'
    POSTGRES_HOST = 'db'
    # DATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@db/{os.environ['POSTGRES_DB']}"
    DATABASE_POOL_SIZE = 10


    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "../env/local.env")
        env_file_encoding = 'utf-8'

