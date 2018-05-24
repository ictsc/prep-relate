from base_settings import *

SECRET_KEY = '<CHANGE ME TO SOME RANDOM STRING ONCE IN PRODUCTION>'

ALLOWED_HOSTS = [
        "*",
        ]

# Configure the following as url as above.
RELATE_BASE_URL = "http://YOUR/RELATE/SITE/DOMAIN"

RELATE_CUTOMIZED_SITE_NAME = gettext_noop("ICTSC PREP SCHOOL")

# Uncomment this to use a real database. If left commented out, a local SQLite3
# database will be used, which is not recommended for production use.
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'relate',
#         'USER': 'relate',
#         'PASSWORD': '<PASSWORD>',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TIME_ZONE = "Asia/Tokyo"

# {{{ sign-in methods

RELATE_SIGN_IN_BY_EMAIL_ENABLED = False
RELATE_SIGN_IN_BY_USERNAME_ENABLED = True
RELATE_REGISTRATION_ENABLED = False
RELATE_SIGN_IN_BY_EXAM_TICKETS_ENABLED = False
