#!/bin/bash

# Apply database migrations
echo "Apply database migrations:"
python manage.py migrate --noinput

# Create superuser
echo "Create superuser:"
python manage.py autocreatesuperuser

# Start server
echo "Starting server:"
python manage.py runserver 0.0.0.0:8000