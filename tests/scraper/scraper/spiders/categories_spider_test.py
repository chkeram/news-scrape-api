from unittest import TestCase
from scrapy.http import HtmlResponse
from scrapy.utils.test import get_crawler
from scraper.scraper.spiders.categories_spider import GuardianCategorySpider


class TestGuardianCategorySpider(TestCase):
    def setUp(self):
        self.spider = GuardianCategorySpider()
        self.crawler = get_crawler(self.spider.__class__)

    def test_parse(self):
        from scrapy.http import HtmlResponse
        html = """
        <ul class="menu-group menu-group--secondary">
            <li class="menu-item">
                <a class="menu-item__title" href="https://www.theguardian.com/uk-news">UK news</a>
            </li>
            <li class="menu-item">
                <a class="menu-item__title" href="https://www.theguardian.com/world">World news</a>
            </li>
        </ul>
        """
        response = HtmlResponse(url="https://www.theguardian.com/international", body=html, encoding="utf-8")
        results = list(self.spider.parse(response))

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["source"], "The Guardian")
        self.assertEqual(results[0]["category_urls"], ["https://www.theguardian.com/uk-news", "https://www.theguardian.com/world"])
