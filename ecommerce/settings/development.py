from .default import *
from dotenv import load_dotenv
import os

load_dotenv()
DEBUG = os.environ.get('DEBUG')
PRODUCTION = os.environ.get('PRODUCTION')
SECRET_KEY = os.environ.get('SECRET_KEY')
WSGI_APPLICATION = 'ecommerce.wsgi.development.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfields')
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafields')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]
