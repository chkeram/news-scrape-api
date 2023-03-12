from unittest import TestCase
import requests
import vcr
import os
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

    @vcr.use_cassette(
        os.path.join(os.path.dirname(__file__), "cassettes/TestGuardianCategorySpider.test_parse_real_data.yml")
    )
    def test_parse_real_data(self):
        from scrapy.http import HtmlResponse

        re = requests.get("https://www.theguardian.com/international")
        response = HtmlResponse(url="https://www.theguardian.com/international", body=re.content, encoding="utf-8")
        results = list(self.spider.parse(response))
        print(results)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["source"], "The Guardian")
        self.assertEqual(results[0]["category_urls"][:3],
                         ['https://www.theguardian.com/world', 'https://www.theguardian.com/uk-news',
                          'https://www.theguardian.com/world/coronavirus-outbreak'])
