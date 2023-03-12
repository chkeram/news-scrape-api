import scrapy
import json
from typing import List
from functools import lru_cache
from pydantic import BaseModel
from scraper.general_settings import get_settings

settings = get_settings()


class CategoryUrls(BaseModel):
    source: str
    category_urls: List[str]


@lru_cache()
def parse_category_links(file_path: str):
    with open(file_path) as f:
        return json.load(f)


def category_links_per_source(category_filter: str) -> CategoryUrls:
    categories = parse_category_links(file_path=settings.CATEGORIES_FILE)

    for item in categories:
        if item['source'] == category_filter:
            return CategoryUrls.parse_obj(item)


class GuardianArticleLinkSpider(scrapy.Spider):
    name = 'article_links'

    categories = category_links_per_source('The Guardian')
    start_urls = categories.category_urls
    source = categories.source

    def parse(self, response):

        for article in response.css('a[data-link-name="article"]'):
            title = article.css('a.u-faux-block-link__overlay.js-headline-text::text').get()
            if title:
                yield {
                    # TODO: parse genre from url
                    'genre': response.url.split('/')[-1],
                    'headline': title,
                    'url': article.css('a.u-faux-block-link__overlay.js-headline-text::attr(href)').get(),
                    'source': self.source
                }


if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    import json
    from scraper.general_settings import get_settings

    scraper_settings = get_settings()
    process = CrawlerProcess(settings={
        'FEED_URI': f"{scraper_settings.ARTICLE_LINKS_FILE}",
        'FEEDS': {
            f"{scraper_settings.ARTICLE_LINKS_FILE}": {
                'format': 'json',
                'encoding': 'utf8',
                'overwrite': True
            }
        }
    })
    process.crawl(GuardianArticleLinkSpider)
    process.start()


