from .base import *
import os


# Disable debug mode

DEBUG = False
TEMPLATE_DEBUG = False


# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_OFFLINE = True


# Send notification emails as a background task using Celery,
# to prevent this from blocking web server threads
# (requires the django-celery package):
# http://celery.readthedocs.org/en/latest/configuration.html

# import djcelery
#
# djcelery.setup_loader()
#
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'redis://'


# Use Redis as the cache backend for extra performance
# (requires the django-redis-cache package):
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#cache

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'KEY_PREFIX': 'base',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
#         }
#     }
# }

# Setup for CAS
ENABLE_SSO = True

MIDDLEWARE_CLASSES += (
    'molo.core.middleware.MoloCASMiddleware',
    'molo.core.middleware.Custom403Middleware',
)


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'molo.core.backends.MoloCASBackend',
)

AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME', None)  # noqa: F405
AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY', None)  # noqa: F405
AZURE_CONTAINER = os.environ.get('AZURE_CONTAINER', None)  # noqa: F405
AZURE_SSL = True

if AZURE_ACCOUNT_NAME and AZURE_ACCOUNT_KEY and AZURE_CONTAINER:
    DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'

CAS_SERVER_URL = ''
CAS_ADMIN_PREFIX = '/admin/'
LOGIN_URL = '/accounts/login/'
CAS_VERSION = '3'

try:
    from .local import *
except ImportError:
    pass
