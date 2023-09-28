FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r ./requirements.txt

COPY ./src /app/

ENV PYTHONPATH "/usr/bin/python3:/usr/src/app"
