from base_settings import *

SECRET_KEY = '<CHANGE ME TO SOME RANDOM STRING ONCE IN PRODUCTION>'

ALLOWED_HOSTS = [
        "*",
        ]

CSRF_TRUSTED_ORIGINS = [
        ".prep.icttoracon.net",
]

# Configure the following as url as above.
RELATE_BASE_URL = "http://YOUR/RELATE/SITE/DOMAIN"

RELATE_CUTOMIZED_SITE_NAME = gettext_noop("ICTSC PREP SCHOOL")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'relate',
        'USER': 'relate',
        'PASSWORD': '',
        'HOST': 'db.prep.icttoracon.net',
        'PORT': '5432',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TIME_ZONE = "Asia/Tokyo"

# {{{ sign-in methods

RELATE_SIGN_IN_BY_EMAIL_ENABLED = False
RELATE_SIGN_IN_BY_USERNAME_ENABLED = True
RELATE_REGISTRATION_ENABLED = False
RELATE_SIGN_IN_BY_EXAM_TICKETS_ENABLED = False
