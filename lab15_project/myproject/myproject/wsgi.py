"""
WSGI config for myproject project.

WSGI (Web Server Gateway Interface) - веб-сервер мен Django қолданбасы
арасындағы стандартты интерфейс. Gunicorn осы файл арқылы Django-ны іске қосады.

Gunicorn команда мысалы:
    gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()
