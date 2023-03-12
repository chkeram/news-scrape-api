#!/bin/bash -e

docker-compose run --rm scraper bash -c \
"scrapy runspider scraper/scraper/spiders/categories_spider.py -O scraper/scraper/output/categories.json;
scrapy runspider scraper/scraper/spiders/article_links_spider.py -O scraper/scraper/output/article_links.json;
scrapy runspider scraper/scraper/spiders/article_spider.py -O scraper/scraper/output/articles.json;
"
