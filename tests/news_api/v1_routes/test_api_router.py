import json
import pytest

from news_api.data.schemas import Article
from tests.news_api.data.test_models import TestModels

# noinspection PyUnresolvedReferences
from tests.news_api.test_main import news_api_test_app
from tests.news_api.data.test_models import db_session, valid_article

mock_article = Article(body="body2", author="author", headline="headline", url="url", genre="genre", source="source")


def get_mock_input():
    return {
        "body": "Test body of article",
        "author": "Mr. Bean",
        "headline": "New Hot Article",
        "url": "London",
        "address": "some address",
        "logo_url": "https://www.theguardian.com/commentisfree/2023/mar/01/people-sleep-rough-britain-streets-rishi-sunak-tories",
        "genre": "opinions",
        "source": "The Guardian"
    }


def add_seed_to_db():
    models = TestModels()
    models.test_article_valid(db_session, valid_article)


@pytest.fixture(scope="module")
def test_get_all_articles_with_mock_results(news_api_test_app):
    add_seed_to_db()
    route = f'/v1/all-news?limit=7&offset=0'
    response = news_api_test_app.get(f'{route}')
    assert valid_article == Article.parse_raw(response.text)


def test_post_article(news_api_test_app):
    response = news_api_test_app.post(f"/v1/", data=json.dumps(get_mock_input()))
    expected = Article.parse_obj(get_mock_input())
    assert response.status_code == 201
    assert expected == Article.parse_raw(response.text)


