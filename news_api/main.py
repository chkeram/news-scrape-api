import logging.config
import os

from fastapi import FastAPI, status, Depends
from fastapi_sqlalchemy import DBSessionMiddleware, db

from news_api.dependencies import get_settings
from news_api.v1_routes import api_router as v1

from news_api.data.session import get_db
from news_api.data import models
from news_api.data.session import engine

models.Base.metadata.create_all(bind=engine)

V1_PREFIX = "/v1"
dir_name = os.path.dirname(__file__)
settings = get_settings()


def get_application():
    logging.config.fileConfig(f"{dir_name}/logging.ini", disable_existing_loggers=False)
    logging.basicConfig(level=logging.INFO)
    _app = FastAPI(title=get_settings().PROJECT_NAME, dependencies=[Depends(get_settings)])

    return _app


app = get_application()
app.include_router(v1.router,
                   dependencies=[Depends(get_settings), Depends(get_db)],
                   # dependencies=[Depends(get_settings)],
                   prefix=V1_PREFIX, tags=["news-api"])

# app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)


@app.get("/_healthcheck", status_code=status.HTTP_200_OK)
def healthcheck():
    return {"status": "OK"}


# @app.on_event("startup")
# def startup():
#     check_redis_connection(redis_cache=get_redis_cache(), settings=get_settings())
#     logging.info("Startup")
#
#
# @app.on_event("shutdown")
# def shutdown():
#     get_redis_cache().close()
#     logging.info("Shutdown")
