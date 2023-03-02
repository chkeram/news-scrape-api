FROM python:3.10-slim as python-base
ENV WORKDIR=/app
ENV PYTHONPATH="${PYTHONPATH}:${WORKDIR}:${WORKDIR}/lib"

WORKDIR $WORKDIR
COPY requirements.txt ./
RUN pip install --upgrade pip \
 && apt-get update && apt-get install -y libpq-dev gcc \
 && pip install -r requirements.txt \
 && apt-get purge -y libpq-dev gcc

FROM python-base
ENV PORT=3000
EXPOSE 3000
COPY news_api $WORKDIR/news-api
#COPY ./tests $WORKDIR/tests
WORKDIR /app/api_reporting

CMD ddtrace-run hypercorn news_api.main:app --bind 0.0.0.0:${PORT}
