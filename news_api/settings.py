import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "news-api"
    PROJECT_VERSION = 1.0
    DOMAIN_ENV: str = "development"
    MOCK_API_CALLS_FOR_TESTS = False
    DATABASE_URL = "postgresql://postgres:password@core-db:5432/dev"
    DATABASE_POOL_SIZE = 10

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "../env/local.env")
        env_file_encoding = 'utf-8'
