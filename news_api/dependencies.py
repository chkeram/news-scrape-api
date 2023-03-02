from functools import lru_cache


from news_api.settings import Settings


@lru_cache()
def get_settings() -> Settings:
    return Settings()


# @lru_cache()
# def get_big_query_data_store() -> BigQueryDataStore:
#     return BigQueryDataStore(get_settings(), redis_cache=get_redis_cache())
#
#
# @lru_cache()
# def get_redis_cache() -> redis.Redis:
#     return redis.Redis.from_url(get_settings().REDIS_URL, decode_responses=True,
#                                 retry_on_error=[ConnectionError, TimeoutError])
#
#
# @lru_cache()
# def get_bigquery_repo() -> BigqueryRepo:
#     settings = get_settings()
#     if settings.MOCK_API_CALLS_FOR_TESTS:
#         return BigqueryRepoDev(settings)
#     return BigqueryRepo(get_settings(), redis_cache=get_redis_cache())


# @lru_cache()
# def get_core_api_client() -> CoreApi:
#     settings = get_settings()
#     if settings.MOCK_API_CALLS_FOR_TESTS:
#         return CoreApiDev(settings=settings)
#     return CoreApi(token_factory=TokenFactory(settings=settings), settings=settings)
