"""
Django settings for myproject project.
Зертханалық жұмыс №15 - Жобаны орналастыруға дайындау
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# .env файлын жүктеу
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================================
# ҚАУІПСІЗДІК ПАРАМЕТРЛЕРІ (Security Settings)
# ============================================================

# SECRET_KEY - .env файлынан жүктелді (құпия ақпарат!)
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key-only-for-dev')

# DEBUG - өндірісте МІНДЕТТІ ТҮРДЕ False болуы керек
# True кезінде: толық қате мәліметтері браузерде көрсетіледі
# False кезінде: қателер жасырылып, 500 бет қайтарылады
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS - Django қай хосттарға жауап беретінін анықтайды
# Бұл параметр HTTP Host header атакаларынан қорғайды
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# ============================================================
# ҚОЛДАНБА КОНФИГУРАЦИЯСЫ (Application Definition)
# ============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI конфигурациясы - Gunicorn осы файл арқылы Django-ға қосылады
WSGI_APPLICATION = 'myproject.wsgi.application'

# ============================================================
# ДЕРЕКҚОР КОНФИГУРАЦИЯСЫ (Database)
# ============================================================

# Барлық дерекқор мәліметтері .env файлынан жүктеледі
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('DB_USER', ''),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', ''),
    }
}

# ============================================================
# СТАТИКАЛЫҚ ФАЙЛДАР (Static Files)
# ============================================================

# STATIC_URL - браузер статикалық файлдарға қандай URL арқылы жетеді
STATIC_URL = '/static/'

# STATICFILES_DIRS - жобадағы статикалық файлдар орналасқан қалталар
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# STATIC_ROOT - 'python manage.py collectstatic' командасы
# барлық статикалық файлдарды осы қалтаға жинайды.
# Nginx осы қалтадан статикалық файлдарды тікелей береді.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Медиа файлдар
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ============================================================
# ҚОСЫМША ҚАУІПСІЗДІК БАПТАУЛАРЫ (Production Security)
# ============================================================

# HTTPS арқылы ғана cookie жіберу
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# Clickjacking қорғанысы
X_FRAME_OPTIONS = 'DENY'

# HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
SECURE_SSL_REDIRECT = not DEBUG

# ============================================================
# ЛОКАЛИЗАЦИЯ (Internationalization)
# ============================================================

LANGUAGE_CODE = 'kk'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
