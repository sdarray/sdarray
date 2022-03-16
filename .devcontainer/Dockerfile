FROM --platform=linux/amd64 python:3.8-slim

ENV PATH=$PATH:/root/.local/bin
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update \
    && apt-get install -y curl git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python -
