from .base import *

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, 'static/')
     ]


DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'DeryaMakine',

        'USER': 'postgres',

        'PASSWORD': '123',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}