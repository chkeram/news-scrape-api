# news-scrape-api



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


