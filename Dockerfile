FROM python:3.10-slim as python-base

ENV PYTHONPATH="${PYTHONPATH}:${WORKDIR}:${WORKDIR}/lib"

ENV WORKDIR=/app
WORKDIR $WORKDIR

COPY requirements.txt ./

RUN apt-get clean && apt-get update && apt-get install -y libpq-dev libyaml-dev gcc libgeos-dev \
&& pip install --upgrade pip \
&& pip install -r requirements.txt \
&& apt-get purge -y libpq-dev gcc

FROM python-base

WORKDIR $WORKDIR
COPY news_api $WORKDIR/news-api
COPY scraper $WORKDIR/scraper
COPY ./tests $WORKDIR/tests
EXPOSE 3000
CMD hypercorn news_api.main:app --reload --bind 0.0.0.0:3000
