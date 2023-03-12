import scrapy
import json
from typing import List
from functools import lru_cache
from pydantic import BaseModel
from scraper.settings import get_settings

settings = get_settings()


class ArticleLink(BaseModel):
    source: str
    genre: str
    headline: str
    url: str


@lru_cache()
def parse_category_links(file_path: str):
    with open(file_path) as f:
        return json.load(f)


def article_links_per_source(category_filter: str) -> List[ArticleLink]:
    categories = parse_category_links(file_path=f'{settings.OUTPUT_DIR}/article_links.json')

    article_links = []
    for item in categories:
        if item['source'] == category_filter:
            article_links.append(ArticleLink.parse_obj(item))

    return article_links


class GuardianArticleSpider(scrapy.Spider):
    name = 'article'

    article_links = article_links_per_source('The Guardian')
    start_urls = [article.url for article in article_links]

    def parse(self, response):
        # Set article_links field to corresponding value from self.article_links
        article_link = self.article_links[len(self.crawler.engine.slot.scheduler)]

        author = response.css('address[aria-label="Contributor info"] a::text').getall()
        main_content = response.css('div[id="maincontent"]')
        paragraphs = main_content.css("p::text").getall()
        content = "".join(paragraphs)
        yield {
            # TODO: headline & genre from article_links_spider.py json output
            "headline": article_link.headline,
            "genre": article_link.genre,
            "author": author,
            "url": response.url,
            "source": article_link.source,
            "body": content
        }


if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    import json
    from scraper.settings import get_settings

    scraper_settings = get_settings()
    process = CrawlerProcess(settings={
        'FEEDS': {
            f"{scraper_settings.OUTPUT_DIR}/articles.json": {
                'format': 'json',
                'encoding': 'utf8',
                'overwrite': True
            }
        }
    })
    process.crawl(GuardianArticleSpider)
    process.start()
