import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
import logging

from scraper.general_settings import get_settings
from scraper.store_articles.model import Article

settings = get_settings()

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

logger = logging.getLogger(__name__)


class NewsApiClient:
    def __init__(self):
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST"], backoff_factor=0.2, respect_retry_after_header=True
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)
        http.mount("http://", adapter)
        self.news_api_base_uri = settings.NEWS_API_BASE_URL
        self.http = http
        self.headers = headers

    def post_article(self, article: Article):
        url = f"{self.news_api_base_uri}/news"
        try:
            req = self.http.post(url,
                                 data=article.json(),
                                 headers=self.headers)
            if req.status_code == 201:
                logger.info("Article posted successfully")
            else:
                logger.error(f"NewsApiClient.post_article(): {article} {req.status_code} {req.text}")
        except Exception as e:
            text = f"NewsApiClient.post_article(): {article} {e}"
            logger.exception(text)
