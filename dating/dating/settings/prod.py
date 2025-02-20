import os

from .base import *


ENVIRONMENT = 'prod'

DEBUG = True

ADMINS = [
    ("Maksim S", os.environ.get('ADMIN_EMAIL'))
]

ALLOWED_HOSTS = ['*']

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.environ.get('POSTGRES_PORT', 5432),
    }
}
