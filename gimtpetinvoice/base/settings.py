import os
import environ
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
)

DJANGO_ENV = env('DJANGO_ENV', default='dev')
env_file_name = 'prod.env' if DJANGO_ENV == 'prod' else 'dev.env'
environ.Env.read_env(os.path.join(BASE_DIR, '..',  env_file_name))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Application definition
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
CUSTOM_APPS = [
    'provider',
    'invoicing'
]

PCKG_APPS = [
    'rest_framework.authtoken',
    'django_filters',
    'django_elasticsearch_dsl',
    'corsheaders',
    'django_celery_results',
    'shell_plus'
]

INSTALLED_APPS = BASE_APPS + CUSTOM_APPS + PCKG_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DATABASE_NAME"),
        'USER': env("DATABASE_USER"),
        'PASSWORD': env("DATABASE_PASS"),
        'HOST': env("DATABASE_HOST"),
        'PORT': env("DATABASE_PORT")
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}

# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

}


ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'localhost:9200'
    },
}


LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
      'simple': {
            'format': '%(message)s'
        },
  },
  'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logstash': {
            'level': 'WARNING',
            'class': 'logstash.TCPLogstashHandler',
            'host': 'localhost',
            'port': 5959, # Default value: 5959
            'version': 1, # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
            'message_type': 'django',  # 'type' field in logstash message. Default value: 'logstash'.
            'fqdn': False, # Fully qualified domain name. Default value: false.
            'tags': ['django.request'], # list of tags. Default: None.
        },
  },
  'loggers': {
        'django.request': {
            'handlers': ['logstash'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
    }
}

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

from kombu import Exchange, Queue
CELERY_TASK_ROUTES = {
 'invoicing.tasks.*': {'queue': 'default'},
 'provider.tasks.*': {'queue': 'default'},
}

CELERY_TASK_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)

CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH=191
