# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
from os import environ

DATABASES = {
    'default': {
        'ENGINE': environ['DB_ENGINE'],
        'NAME': environ['DB_NAME'],
        'USER': environ['DB_USER'],
        'PASSWORD': environ['DB_PASSWORD'],
        'HOST': environ['DB_HOST'],
        'PORT': environ['DB_PORT'],
    },
}
