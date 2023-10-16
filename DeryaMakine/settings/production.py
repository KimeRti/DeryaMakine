from .base import *

DEBUG = False

ALLOWED_HOSTS = ['www.deryamakine.com', 'deryamakine.com']

STATIC_ROOT = 'DeryaMakine/static/'

CSRF_TRUSTED_ORIGINS = ['www.deryamakine.com', 'deryamakine.com']
CORS_ALLOWED_ORIGINS = ['www.deryamakine.com', 'deryamakine.com']
CORS_ALLOWED_ORIGIN_REGEXES = ['www.deryamakine.com', 'deryamakine.com']
CORS_ALLOW_ALL_ORIGINS = ['www.deryamakine.com', 'deryamakine.com']