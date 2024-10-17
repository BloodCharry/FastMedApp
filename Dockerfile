FROM python:3.11.5

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    postgresql \
    gcc \
    python3-dev \
    musl-dev \
    && apt-get upgrade -y \
    && pip install --upgrade pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /usr/src/app/

RUN poetry install

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
