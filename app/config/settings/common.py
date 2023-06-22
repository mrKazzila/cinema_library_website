from os import environ
from pathlib import Path

from dotenv import load_dotenv

# Path settings
BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = BASE_DIR.resolve().parent
ROOT_DIR = BASE_DIR.resolve().parent.parent
ENV_DIR = Path(ROOT_DIR / 'env')

# Env settings
dotenv_path = ENV_DIR / '.env.project'
load_dotenv(dotenv_path)

# Base project settings
DEBUG = environ['DJANGO_DEBUG']
SECRET_KEY = environ['DJANGO_SECRET_KEY']
ALLOWED_HOSTS = environ['DJANGO_ALLOWED_HOSTS'].split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    # Third party apps
    'ckeditor',
    'ckeditor_uploader',
    'snowpenguin.django.recaptcha3',
    'allauth',
    'allauth.account',

    # My apps
    'cinemalib.apps.CinemalibConfig',
    'subscription.apps.SubscriptionConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            APPS_DIR / 'cinemalib/templates',
            APPS_DIR / 'subscription/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = ROOT_DIR / 'static'
STATICFILES_DIRS = (APPS_DIR / 'static',)

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = ROOT_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

SITE_ID = 1
