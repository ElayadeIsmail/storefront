from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-*-tzv7mx$4pw%d1zr!@k-awe+6gr)e9r)u$82_&i+dxbxuhugb'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'HOST': env("DB_HOST"),
        'PORT': env.int('DB_PORT'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD')
    }
}
