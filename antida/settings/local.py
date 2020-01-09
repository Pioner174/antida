from .base import *

DEBUG = True

SECRET_KEY = '3o)pf7u7en82d5dg8c%a1+l_+6@vt+y*!2lx0@t_(dxccbs$q_'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': '2505',
    }
}