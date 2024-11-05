FROM python:3.11.5

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    gcc \
    musl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /usr/src/app/
RUN poetry install

COPY ./entrypoint.sh /usr/src/app/
COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
