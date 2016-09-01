web: gunicorn wsgi:application
worker: celery -A fossevents worker -l info --concurrency=2 -B
