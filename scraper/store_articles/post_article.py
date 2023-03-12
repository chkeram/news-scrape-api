from scraper.store_articles.news_api_client import NewsApiClient
from scraper.store_articles.model import Article
from scraper.general_settings import get_settings
import json
import logging

logger = logging.getLogger(__name__)

settings = get_settings()


def post_articles():
    logger.info("Posting Articles to news api started:")
    api_client = NewsApiClient()

    with open(settings.ARTICLES_FILE) as f:
        logger.info("Fetching articles from file")
        articles_json = json.load(f)

    articles = []
    for article in articles_json:
        articles.append(Article(**article))
        api_client.post_article(article)
