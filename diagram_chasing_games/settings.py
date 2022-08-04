"""
Django settings for diagram_chasing_games project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = Path(__file__).resolve().parent.parent
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'TODO: use secret key in deployment')

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('ON_HEROKU', '0') == '0':
    DEBUG = True
else:
    DEBUG = False

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    # TODO comment out

ALLOWED_HOSTS = [
    '127.0.0.1',
    #'database-of-proofs-engine.herokuapp.com/',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'whitenoise.runserver_nostatic',
    'django_bootstrap5',
    'cd_editor.apps.CdEditorConfig',
    'database.apps.DatabaseConfig',
    'django_neomodel',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'diagram_chasing_games.urls'

TEMPLATES_PATH = os.path.join(SETTINGS_PATH, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_PATH, 
                 os.path.join(TEMPLATES_PATH, 'diagram_chasing_games'),
                 os.path.join(TEMPLATES_PATH, 'accounts'),
                 os.path.join(TEMPLATES_PATH, 'cd_editor'),
                 os.path.join(TEMPLATES_PATH, 'database')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'diagram_chasing_games.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# TODO: try out PostgreSQL in production, i.e. change True to the commented out code;
if os.environ.get('ON_HEROKU', '0') == '0':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        # TODO: what does this max_age setting do?
        'default' : dj_database_url.config(conn_max_age=600)
    }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(SITE_ROOT, 'static/'),)

def neo4j_url():
    url = os.environ.get('NEO4J_SCHEMA', 'bolt') + "://"
    url += os.environ.get('NEO4J_USERNAME', 'neo4j') + ":"
    url += os.environ.get('NEO4J_PASSWORD', 'fusion123') + "@"
    url += os.environ.get('NEO4J_HOST', 'localhost') + ":"
    url += os.environ.get('NEO4J_PORT', '7687')
    return url

NEOMODEL_NEO4J_BOLT_URL = neo4j_url()

NEOMODEL_SIGNALS = True
NEOMODEL_FORCE_TIMEZONE = False
NEOMODEL_ENCRYPTED_CONNECTION = False  # TODO: how do we switch this on without error?

from neomodel import config   # BUGFIX: had to do it this way
config.MAX_POOL_SIZE = 50  # TODO: what does this affect?

#LOGIN_REDIRECT_URL = 'home'
#LOGOUT_REDIRECT_URL = 'home'

# TODO: Enable Click-jacking protection
X_FRAME_OPTIONS = 'ALLOW'   # ie set this to "DENY"
# https://docs.djangoproject.com/en/1.11/ref/clickjacking/

MAX_NAME_LENGTH = 64
MAX_DIAGRAM_NAME_LENGTH = MAX_NAME_LENGTH
MAX_USERNAME_LENGTH = MAX_NAME_LENGTH
MAX_CODE_LENGTH = 4096
MAX_GLOBAL_DICT_LENGTH = 512
MAX_PASSWORD_LENGTH = 128
MAX_TEXT_LENGTH = 123

MAX_USER_EDIT_DIAGRAMS = 8
MAX_BAD_CONN_RETRIES = 5

# Activate Django-Heroku.
django_heroku.settings(locals())

#MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'