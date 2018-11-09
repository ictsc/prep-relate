from base_settings import *

SECRET_KEY = '<CHANGE ME TO SOME RANDOM STRING ONCE IN PRODUCTION>'

ALLOWED_HOSTS = [
        "*",
        ]

STATIC_URL = '/relate/static/'

CSRF_TRUSTED_ORIGINS = [
        ".prep-dev.icttoracon.net",
]

# Configure the following as url as above.
RELATE_BASE_URL = "http://YOUR/RELATE/SITE/DOMAIN"

RELATE_CUTOMIZED_SITE_NAME = gettext_noop("ICTSC PREP SCHOOL")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'relate',
        'USER': 'relate',
        'PASSWORD': 'iCtsC2O18',
        'HOST': 'db.prep-dev.icttoracon.net',
        'PORT': '5432',
    }
}

# {{{ git storage

# Your course git repositories will be stored under this directory.
# Make sure it's writable by your web user.
#
# The default below makes them sit side-by-side with your relate checkout,
# which makes sense for development, but you probably want to change this
# in production.
#
# The 'course identifiers' you enter will be directory names below this root.

# GIT_ROOT = "/some/where"
GIT_ROOT = "/var"

# }}}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TIME_ZONE = "Asia/Tokyo"

# {{{ sign-in methods

RELATE_SIGN_IN_BY_EMAIL_ENABLED = False
RELATE_SIGN_IN_BY_USERNAME_ENABLED = True
RELATE_REGISTRATION_ENABLED = False
RELATE_SIGN_IN_BY_EXAM_TICKETS_ENABLED = False
