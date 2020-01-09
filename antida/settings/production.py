from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ADMINS = [
    ('Matanin R', 'Romashka951@gmail.com')
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['NAME'],
        'HOST': os.environ['HOST'],
        'PORT': os.environ['PORT'],
        'USER': os.environ['USER'],
        'PASSWORD': os.environ['PASSWORD'],
    }
}

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 3600

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

SECURE_REFERRER_POLICY = 'unsafe-url'


