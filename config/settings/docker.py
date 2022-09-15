from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}

# CELERY STUFF
CELERY_BROKER_URL = 'amqp://user:password@rabbitmq:5672/celery_tasks'

DEFAULT_FROM_EMAIL = 'from@mysite.com'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = '/static/'
