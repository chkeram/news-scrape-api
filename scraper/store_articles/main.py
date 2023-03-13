from scraper.store_articles.news_api_client import NewsApiClient
from scraper.store_articles.model import Article
from scraper.general_settings import get_settings
import json
import logging

logger = logging.getLogger(__name__)

settings = get_settings()


def post_articles():
    logger.info("scraper.main.post_articles(): Posting Articles to News api started:")
    api_client = NewsApiClient()

    with open(settings.ARTICLES_FILE) as f:
        logger.info("scraper.main.post_articles(): Fetching articles from file")
        articles_json = json.load(f)

    articles = []
    for article in articles_json:
        art = Article(**article)
        articles.append(art)
        api_client.post_article(art)
        logger.info(f"scraper.main.post_articles(): Posting article: {art.headline}")
        print(f"scraper.main.post_articles(): Posting article: {art.headline}")

    logger.info(f"scraper.main.post_articles(): Posting articles finished. Total articles posted: {len(articles)}")
    print(f"scraper.main.post_articles(): Posting articles finished. Total articles posted: {len(articles)}")


post_articles()


