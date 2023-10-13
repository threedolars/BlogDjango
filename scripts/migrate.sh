#!/bin/sh
makemigrations.sh
echo 'Executing Migrate'
python manage.py migrate  --noinput