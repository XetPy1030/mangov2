import os

from django.conf.global_settings import *

INSTALLED_APPS = [
    'database.apps.DatabaseConfig',
]

ALLOWED_HOSTS = ['*']
DEBUG = True

DJANGO_SETTINGS_MODULE = 'database.settings'

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
