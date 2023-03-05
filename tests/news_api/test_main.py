import pytest
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from news_api.dependencies import get_settings
from news_api.main import get_application
from news_api.v1_routes import api_router as v1
from news_api.data.session import get_db

V1_PREFIX = "/v1"


def get_settings_for_test():
    settings = get_settings()
    settings.MOCK_API_CALLS_FOR_TESTS = True
    # settings.POSTGRES_DB = "news_api_test_db"
    # settings.POSTGRES_USER = "news_api_test_user"
    # settings.POSTGRES_PASSWORD = "news_api_test_password"
    return settings

def get_test_session():
    # Create a new engine object with a custom connection URL
    test_engine = create_engine("postgresql://locahost/mydatabase_test")

    # Create a new session factory using the test engine
    TestSession = sessionmaker(bind=test_engine)

    # Return a new session object
    return TestSession()


@pytest.fixture(scope="module")
def news_api_test_app() -> FastAPI:
    app = get_application()
    get_db.override = get_test_session

    # TODO:  add v1.router for v1 routes unittests
    app.include_router(v1.router,
                       # dependencies=[Depends(get_settings_for_test), Depends(get_db)],
                       dependencies=[Depends(get_settings_for_test), Depends(get_test_session)],
                       prefix=V1_PREFIX, tags=["news-api"])
    client = TestClient(app)
    yield client
