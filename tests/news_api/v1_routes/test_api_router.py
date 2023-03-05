import json
import pytest

from news_api.data.schemas import Article
from tests.news_api.data.test_models import TestModels

# noinspection PyUnresolvedReferences
from tests.news_api.test_main import news_api_test_app
from tests.news_api.data.test_models import db_session, valid_article

mock_article = Article(body="body2", author="author", headline="headline", url="url", genre="genre")


def get_mock_input():
    return {
        "body": "Test body of article",
        "author": "Mr. Bean",
        "headline": "New Hot Article",
        "url": "London",
        "address": "some address",
        "logo_url": "https://www.theguardian.com/commentisfree/2023/mar/01/people-sleep-rough-britain-streets-rishi-sunak-tories",
        "genre": "opinions"
    }

# def add_seed_to_db(news_api_test_app):
#     # TODO: replace the below with adding a seed to the db directly
#
#     response = news_api_test_app.post(f"/v1/", data=json.dumps(get_mock_input()))
#     assert response.status_code == 201
#     # return Article.parse_raw(response.text)


@pytest.fixture(scope="module")
def test_get_all_articles_with_mock_results(news_api_test_app):
    models = TestModels()
    expected = models.test_article_valid(db_session, valid_article)
    route = f'/v1/news'
    response = news_api_test_app.get(f'{route}')
    print('-=-=-=-=-=-=-=-=-=- ', response.text)
    assert expected == Article.parse_raw(response.text)


def test_post_article(news_api_test_app):
    response = news_api_test_app.post(f"/v1/", data=json.dumps(get_mock_input()))
    # result = response.json()
    expected = Article.parse_obj(get_mock_input())
    assert response.status_code == 201
    assert expected == Article.parse_raw(response.text)


