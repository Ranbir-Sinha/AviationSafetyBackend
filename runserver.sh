python manage.py makemigrations
python manage.py migrate
python manage.py sync_data
python manage.py test api

# LOCAL
#python manage.py runserver

# PRODUCTION
gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 AviationSafetyBackend.wsgi:application
