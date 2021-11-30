#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn --reload tdd_django.wsgi:application \
    --bind 0.0.0.0:8000
