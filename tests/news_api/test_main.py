import pytest
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from news_api.dependencies import get_settings
from news_api.main import get_application
# from api_reporting.session import get_db
from news_api.v1_routes import api_router as v1

V1_PREFIX = "/v1"


def get_settings_for_test():
    settings = get_settings()
    settings.MOCK_API_CALLS_FOR_TESTS = True
    return settings


@pytest.fixture(scope="module")
def news_api_test_app() -> FastAPI:
    app = get_application()

    # TODO:  add v1.router for v1 routes unittests
    app.include_router(v1.router,
                       # dependencies=[Depends(get_settings_for_test), Depends(get_db)],
                       dependencies=[Depends(get_settings_for_test)],
                       prefix=V1_PREFIX, tags=["news-api"])
    client = TestClient(app)
    yield client
