from .base import *


ENVIRONMENT = 'prod'

DEBUG = True

ADMINS = [
    ("Maksim S", os.environ['ADMIN_EMAIL'])
]

ALLOWED_HOSTS = ['*']

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dating',
        'USER': 'dating_suser',
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
