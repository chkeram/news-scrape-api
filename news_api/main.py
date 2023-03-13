import logging.config
import os

from fastapi import FastAPI, status, Depends

from news_api.dependencies import get_settings
from news_api.v1_routes import api_router as v1

from news_api.data.session import get_db
from news_api.data import models
from news_api.data.session import engine, check_postgres_connection


V1_PREFIX = "/v1"
dir_name = os.path.dirname(__file__)
settings = get_settings()


def init_db():
    check_postgres_connection()
    models.Base.metadata.create_all(bind=engine)


def get_application():
    logging.config.fileConfig(f"{dir_name}/logging.ini", disable_existing_loggers=False)
    logging.basicConfig(level=logging.INFO)
    _app = FastAPI(title=get_settings().PROJECT_NAME, dependencies=[Depends(get_settings)])

    return _app


app = get_application()
app.include_router(v1.router,
                   dependencies=[Depends(get_settings), Depends(get_db)],
                   prefix=V1_PREFIX, tags=["news-api"])


@app.get("/_healthcheck", status_code=status.HTTP_200_OK)
def healthcheck():
    return {"status": "OK"}


@app.on_event("startup")
async def startup():
    init_db()
    logging.info("Startup")


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()
    logging.info("Shutdown")
