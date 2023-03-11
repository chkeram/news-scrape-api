import scrapy
# from news_scraper.settings import Settings
# from news_scraper.news_scraper.items import NewsScraperItem
# from scrapy.loader import ItemLoader


class GuardianCategorySpider(scrapy.Spider):
    name = 'categories'
    start_urls = ['https://www.theguardian.com/international']

    def parse(self, response):
        categories = response.css('ul.menu-group.menu-group--secondary')
        links = categories.css('a.menu-item__title::attr(href)').getall()
        # TODO: parse source from settings
        # Source should be from fixed list of sources
        yield {'source': 'The Guardian', 'category_urls': links}


if __name__ == '__main__':
    import scrapy
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess()
    process.crawl(GuardianCategorySpider)
    process.start()
