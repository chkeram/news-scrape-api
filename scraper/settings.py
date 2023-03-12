import os
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    MOCK_API_CALLS_FOR_TESTS = False
    OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "scraper/output")
    CATEGORIES_FILE = f"{OUTPUT_DIR}/categories.json"
    ARTICLE_LINKS_FILE = f"{OUTPUT_DIR}/article_links.json"
    ARTICLE_FILE = f"{OUTPUT_DIR}/article.json"
    SOURCES = ['The Guardian', 'The New York Times', 'The Washington Post']

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "../env/local.env")
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings() -> Settings:
    return Settings()


if __name__ == '__main__':
    print(get_settings().dict())
