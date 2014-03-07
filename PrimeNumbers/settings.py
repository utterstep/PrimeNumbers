"""
Django settings for PrimeNumbers project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$=ju!uliyer$vah=+u(ae&2-g(#+z5hcm2^tfid2lat*va)+^y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'primes',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'PrimeNumbers.urls'

WSGI_APPLICATION = 'PrimeNumbers.wsgi.application'


# Internationalization

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'


# Project-specific

MAX_INDEX = 1000000
