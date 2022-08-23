from .base import *

env = environ.Env()

environ.Env.read_env('../.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env('DEBUG')
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mariadb',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'awasoft12!',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}