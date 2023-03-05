from functools import lru_cache


from news_api.settings import Settings


@lru_cache()
def get_settings() -> Settings:
    return Settings()
