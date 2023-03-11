import scrapy


class GuardianArticleLinkSpider(scrapy.Spider):
    name = 'article_links'
    start_urls = ['https://www.theguardian.com/international']

    def parse(self, response):
        categories = response.css('ul.menu-group.menu-group--secondary')
        links = categories.css('a.menu-item__title::attr(href)').getall()
        yield {'guardian': links}
