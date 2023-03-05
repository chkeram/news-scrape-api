import json

from news_api.settings import Settings


from news_api.data.schemas import Article


# noinspection PyUnresolvedReferences
from tests.news_api.test_main import news_api_test_app

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


def add_seed_to_db(news_api_test_app):
    response = news_api_test_app.post(f"/v1/", data=json.dumps(get_mock_input()))
    assert response.status_code == 201
    # return Article.parse_raw(response.text)


def test_get_all_articles_with_mock_results(news_api_test_app):
    add_seed_to_db(news_api_test_app)
    route = f'/v1/news'
    response = news_api_test_app.get(f'{route}')
    assert Article.parse_obj(get_mock_input()) == Article.parse_raw(response.text)


def test_post_article(news_api_test_app):
    response = news_api_test_app.post(f"/v1/", data=json.dumps(get_mock_input()))
    # result = response.json()
    expected = Article.parse_obj(get_mock_input())
    assert response.status_code == 201
    assert expected == Article.parse_raw(response.text)
