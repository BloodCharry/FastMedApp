#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
  echo "Waiting for postgres at $POSTGRES_HOST:$POSTGRES_PORT..."
  while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Postgres is unavailable - sleeping"
    sleep 2
  done
  echo "PostgreSQL started"
fi

cd /usr/src/app/backend  # Переход в директорию с manage.py

if [ ! -f "manage.py" ]; then
  echo "manage.py not found in /usr/src/app/backend"
  ls -la
fi

poetry run python manage.py flush --no-input
poetry run python manage.py migrate

exec "$@"
