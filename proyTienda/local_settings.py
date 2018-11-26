from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tienda_bd',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT':'5432'
    }
}