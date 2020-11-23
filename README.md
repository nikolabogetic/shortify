# shortify

![Build](https://github.com/nikolabogetic/shortify/workflows/Python%20application/badge.svg)

## Descrtiption
Shortify is a URL shortener, like bit.ly or tinyurl. You can POST the long URL, and the short URL will be returned. Following the short URL will issue a redirect to the full URL.



## Usage

It is recommended to set a database password in `docker-compose.yml`

### Start:


```
$ docker-compose build
$ docker-compose up
```
On startup, please wait until you see the message:
```
docker-compose-wait - Everything's fine, the application can now start!
```

On the first run, Postgres needs time to initialize the database. To avoid errors, the app waits until Postgres is ready. Default wait time is 5 seconds, can be overwriten in `docker-compose.yml`



### Make requests:
```
# Submit long URL, get short URL
curl -X POST 'http://127.0.0.1:8080/submit' \
--header 'Content-Type: text/plain' \
--data-raw 'https://www.wikipedia.org/'

# Check redirect message
curl -X GET 'http://127.0.0.1:8080/48VIcsBN5UX'
```

