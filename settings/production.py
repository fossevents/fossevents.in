# -*- coding: utf-8 -*-
'''Production Configurations

- Use djangosecure
- Use Amazon's S3 for storing static files and uploaded media
- Use sendgrid to send emails
- Use MEMCACHIER on Heroku
'''

from .common import *  # noqa


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANO_SECRET_KEY not in os.environ
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
# END SITE CONFIGURATION

INSTALLED_APPS += ("gunicorn", )

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
                         default='FOSS-Events <noreply@fossevents.in>')
EMAIL_HOST = env("DJANGO_EMAIL_HOST", default='smtp.sendgrid.com')
EMAIL_HOST_PASSWORD = env("SENDGRID_PASSWORD")
EMAIL_HOST_USER = env('SENDGRID_USERNAME')
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_SUBJECT_PREFIX = env("EMAIL_SUBJECT_PREFIX", default='[FOSS-Events] ')
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
