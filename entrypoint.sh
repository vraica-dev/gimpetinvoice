#!/bin/sh

# Only run in production
if [ "$DJANGO_ENV" = "prod" ]; then
    echo "Running entrypoint for production..."
    python manage.py migrate
    python manage.py collectstatic --noinput
fi

# Start the application
exec "$@"