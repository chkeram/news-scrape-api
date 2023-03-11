import scrapy


class GuardianArticleSpider(scrapy.Spider):
    name = 'article'

    # TODO: urls from article_links_spider.py json output
    start_urls = ['https://www.theguardian.com/global-development/2023/mar/10/children-face-acute-risk-amid-malawis-deadliest-cholera-outbreak']

    def parse(self, response):
        author = response.css('address[aria-label="Contributor info"] a::text').getall()
        main_content = response.css('div[id="maincontent"]')
        paragraphs = main_content.css("p::text").getall()
        content = "".join(paragraphs)
        yield {
            # TODO: headline & genre from article_links_spider.py json output
            "headline": 'headline',
            "genre": 'genre',
            "author": author,
            "body": content,
            "url": response.url,
            #TODO: parse this from settings or json + add it to model
            #"source": "The Guardian"
        }
