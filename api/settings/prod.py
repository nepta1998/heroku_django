import dj_database_url
from decouple import config
from .dev import *
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
ALLOWED_HOSTS = ['*']



