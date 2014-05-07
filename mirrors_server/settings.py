"""
Django settings for mirrors_server project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y#v*j_7ii-r*t#@e^n%nu6*z+0#m(rwy^5u@zs=l&yup(7_gs$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'mirrors_server', 
    'mirrors',
    'scheduler',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mirrors_server.django-crossdomainxhr-middleware.XsSharing',
)

ROOT_URLCONF = 'mirrors_server.urls'

WSGI_APPLICATION = 'mirrors_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# please remember to *not* leave your DB password in source
# control!

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'mirrors_server',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
    }
}


# Logging
# https://docs.djangoproject.com/en/1.6/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log')
        },
        'console': {
            'level':'DEBUG',    
            'class':'logging.StreamHandler',
        },  
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propogate': True
        }
    }
}


# Rest framework
# http://www.django-rest-framework.org/api-guide/testing
REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'locale$',
    'common.views.test', '__init__', 'django',
    'migrations', 'admin$']
