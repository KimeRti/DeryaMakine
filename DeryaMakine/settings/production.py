from .base import *

DEBUG = False

ALLOWED_HOSTS = ['www.deryamakine.com', 'deryamakine.com']

STATIC_ROOT = 'DeryaMakine/static/'

CSRF_TRUSTED_ORIGINS = ['http://www.deryamakine.com', 'http://deryamakine.com', 'https://www.deryamakine.com', 'https://deryamakine.com']
CORS_ALLOWED_ORIGINS = ['http://www.deryamakine.com', 'http://deryamakine.com', 'https://www.deryamakine.com', 'https://deryamakine.com']
CORS_ALLOWED_ORIGIN_REGEXES = ['http://www.deryamakine.com', 'http://deryamakine.com', 'https://www.deryamakine.com', 'https://deryamakine.com']
CORS_ALLOW_ALL_ORIGINS = ['http://www.deryamakine.com', 'http://deryamakine.com', 'https://www.deryamakine.com', 'https://deryamakine.com']

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'deryamakine',

        'USER': 'detexuser',

        'PASSWORD': 'detex123',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}