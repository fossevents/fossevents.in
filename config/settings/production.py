# -*- coding: utf-8 -*-
'''
Production Configurations

- Use djangosecure
- Use Amazon's S3 for storing static files and uploaded media
- Use sendgrid to send emails
- Use MEMCACHIER on Heroku
'''
from __future__ import absolute_import, unicode_literals


# from boto.s3.connection import OrdinaryCallingFormat
# from django.utils import six

from .common import *  # noqa

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANO_SECRET_KEY not in os.environ
SECRET_KEY = env("DJANGO_SECRET_KEY")

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# django-secure
# ------------------------------------------------------------------------------
INSTALLED_APPS += ("djangosecure", )

MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'djangosecure.middleware.SecurityMiddleware',
) + MIDDLEWARE_CLASSES

# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
SECURE_FRAME_DENY = env.bool("DJANGO_SECURE_FRAME_DENY", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
# END SITE CONFIGURATION

INSTALLED_APPS += ("gunicorn", )

# STORAGE CONFIGURATION
# ------------------------------------------------------------------------------
# Uploaded Media Files
# ------------------------
# See: http://django-storages.readthedocs.org/en/latest/index.html
# INSTALLED_APPS += (
#     'storages',
# )
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
# AWS_AUTO_CREATE_BUCKET = True
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

# # AWS cache settings, don't change unless you know what you're doing:
# AWS_EXPIRY = 60 * 60 * 24 * 7

# # TODO See: https://github.com/jschneier/django-storages/issues/47
# # Revert the following and use str after the above-mentioned bug is fixed in
# # either django-storage-redux or boto
# AWS_HEADERS = {
#     'Cache-Control': six.b('max-age=%d, s-maxage=%d, must-revalidate' % (
#         AWS_EXPIRY, AWS_EXPIRY))
# }

# # URL that handles the media served from MEDIA_ROOT, used for managing stored files.
# MEDIA_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME

# Static Assests
# ------------------------
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.cssmin.CSSMinFilter'
]


# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='fossevents <noreply@fossevents.in>')
EMAIL_HOST = env("DJANGO_EMAIL_HOST", default='smtp.sendgrid.com')
EMAIL_HOST_PASSWORD = env("SENDGRID_PASSWORD")
EMAIL_HOST_USER = env('SENDGRID_USERNAME')
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_SUBJECT_PREFIX = env("EMAIL_SUBJECT_PREFIX", default='[fossevents] ')
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
]

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'] = env.db("DATABASE_URL")

# CACHING
# ------------------------------------------------------------------------------
try:
    # Only do this here because thanks to django-pylibmc-sasl and pylibmc
    # memcacheify is painful to install on windows.
    # See: https://github.com/rdegges/django-heroku-memcacheify
    from memcacheify import memcacheify
    CACHES = memcacheify()
except ImportError:
    CACHES = {
        'default': env.cache_url("DJANGO_CACHE_URL", default="memcache://127.0.0.1:11211"),
    }

# Your production stuff: Below this line define 3rd party library settings
