import scrapy


class GuardianCategorySpider(scrapy.Spider):
    name = 'categories'
    start_urls = ['https://www.theguardian.com/international']

    def parse(self, response):
        categories = response.css('ul.menu-group.menu-group--secondary')
        links = categories.css('a.menu-item__title::attr(href)').getall()
        # TODO: parse source from settings

        yield {'source': 'The Guardian', 'category_urls': links}


if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    from scraper.general_settings import get_settings

    scraper_settings = get_settings()
    process = CrawlerProcess(settings={
        'FEED_URI': f"{scraper_settings.CATEGORIES_FILE}",
        'FEEDS': {
            f"{scraper_settings.CATEGORIES_FILE}": {
                'format': 'json',
                'encoding': 'utf8',
                'overwrite': True
            }
        }
    })
    process.crawl(GuardianCategorySpider)
    process.start()
