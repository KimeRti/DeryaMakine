from .base import *

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, '../../static')
     ]

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
