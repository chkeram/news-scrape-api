#!/bin/bash -e

docker-compose run scraper bash -c "python scraper/store_articles/main.py"
