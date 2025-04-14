import os

from .base import *


ENVIRONMENT = 'prod'

DEBUG = False

ADMINS = [
    ("Maksim S", os.environ.get('ADMIN_EMAIL'))
]

ALLOWED_HOSTS = ['127.0.0.1', 'dating-site.com', 'localhost']

CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8090']

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
