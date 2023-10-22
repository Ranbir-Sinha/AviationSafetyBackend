FROM python:3.10.5-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache libxml2-dev libxslt-dev python3-dev gcc build-base jpeg-dev zlib-dev \
    && apk add --no-cache --virtual build-deps musl-dev \
    && apk add --no-cache mariadb-dev \
    && apk add --no-cache cifs-utils

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r /app/requirements.txt
RUN apk del build-deps

COPY . /app

EXPOSE 8000

RUN chmod +x ./runserver.sh
RUN apk add bash
ENTRYPOINT ./runserver.sh
