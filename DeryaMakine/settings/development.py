from .base import *

DEBUG = True

ALLOWED_HOSTS = ['193.38.34.1']

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, 'static/')
     ]


DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'deryamakine',

        'USER': 'kimerti',

        'PASSWORD': 'kimerti123',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}