from scraper.store_articles.news_api_client import NewsApiClient
from scraper.store_articles.model import Article
from scraper.general_settings import get_settings
import json
import logging
import time

logger = logging.getLogger(__name__)

settings = get_settings()


def post_articles():
    logger.info("Posting Articles to news api started:")
    api_client = NewsApiClient()
    # db_art = api_client.get_article()
    # print(db_art)

    with open(settings.ARTICLES_FILE) as f:
        logger.info("Fetching articles from file")
        articles_json = json.load(f)

    articles = []
    for article in articles_json:
        art = Article(**article)
        print('-----')
        articles.append(art)
        api_client.post_article(art)

    print(len(articles))


post_articles()


