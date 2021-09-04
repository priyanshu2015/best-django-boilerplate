from config.settings_base import *


SECRET_KEY = config("SECRET_KEY")

DEBUG=True

ALLOWED_HOSTS=[]

ROOT_URLCONF = 'config.urls'

INSTALLED_APPS += [
]

MIDDLEWARE += [
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # 'second': {

    # }
}

STATIC_URL = '/static/'