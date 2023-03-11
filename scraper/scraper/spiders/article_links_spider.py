import scrapy


class GuardianArticleLinkSpider(scrapy.Spider):
    name = 'article_links'

    # TODO: unpack values from output of categories_spider.py
    start_urls = ['https://www.theguardian.com/world']

    def parse(self, response):

        for article in response.css('a[data-link-name="article"]'):
            title = article.css('a.u-faux-block-link__overlay.js-headline-text::text').get()
            if title:
                yield {
                    # TODO: parse genre from url
                    'genre': response.url.split('/')[-1],
                    'headline': title,
                    'url': article.css('a.u-faux-block-link__overlay.js-headline-text::attr(href)').get(),
                }


if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    import json

    process = CrawlerProcess(settings={
        'FEED_URI': 'output/output.json',
        'FEED_FORMAT': 'json',
    })
    process.crawl(GuardianArticleLinkSpider)
    process.start()

    # Load the output JSON file and write it back without Unicode escape sequences
    with open('output/output.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open('output/output_clean.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)