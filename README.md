# news-scrape-api

## Use Scrapy locally: 

- Install Scrapy: `pip install scrapy`
- You can run scrapy shell for interactive console or run the spiders locally directly

### Run scrapy shell for interactive console

Example: Get the links of all the news categories from theguardian.com
```bash 
>> fetch('https://www.theguardian.com/uk')
>> categories = response.css('ul.menu-group.menu-group--secondary')
>> links = categories.css('a.menu-item__title::attr(href)').getall()
```

### Run the spiders locally directly
- Run the categories_spider.py: 
    ```bash
    scrapy runspider scraper/scraper/spiders/categories_spider.py -O scraper/scraper/output/categories.json
    ```
- Run the article_links_spider.py: 
    ```bash
    scrapy runspider scraper/scraper/spiders/article_spider.py -O scraper/scraper/output/articles.json
  ```
  
- Run the article_spider.py: 
  ```bash
  scrapy runspider scraper/scraper/spiders/article_spider.py -O scraper/scraper/output/articles.json
  ```


## Access Postgres DB using psql

```terminal 
docker-compose exec db psql -U postgres -d mydatabase
>> \dt
>> SELECT * FROM articles;
```

## Access Postgres DB using pgAdmin

- Open pgAdmin in your browser (http://localhost:5050)
- Add a new server
- Set the name to `db`
- Set the host to `db`
- Set the port to `5432`
- Set the username to `postgres`
- Set the password to `postgres`
- Click save


