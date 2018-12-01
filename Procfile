release: python manage.py migrate
web: gunicorn portfolio.wsgi python portfolio/manage.py runserver 0.0.0.0:$PORT --noreload