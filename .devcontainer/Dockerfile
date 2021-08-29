FROM mcr.microsoft.com/vscode/devcontainers/python:3.9
ENV POETRY_VIRTUALENVS_CREATE=false

COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry install
