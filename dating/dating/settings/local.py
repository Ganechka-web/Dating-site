from .base import *


ENVIRONMENT = 'local'

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')
INSTALLED_APPS.append('django_extensions')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

INTERNAL_IPS = [
    '127.0.0.1',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
