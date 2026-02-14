"""
Test Settings for Chew and Cheer

Uses SQLite in-memory database for faster test execution.
Disables external services like Redis, Sentry, and email for isolated testing.
"""
from .settings import *

# Override test runner to exclude UI tests
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Exclude test_ui.py files from Django's test discovery (they run separately with pytest)
import sys
if 'test' in sys.argv:
    TEST_DISCOVER_PATTERN = 'tests.py'

# Use SQLite for tests - much faster than PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Disable password hashers for faster tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Use dummy cache instead of Redis for tests
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Disable logging during tests
LOGGING = {}

# Use in-memory email backend for tests
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Disable Sentry during tests
import sentry_sdk
sentry_sdk.init(dsn=None)

# Disable debug for tests
DEBUG = False

# Use simple file storage for tests (Django 4.2+ STORAGES format)
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
USE_S3 = False

# Disable HTTPS requirements for tests
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Faster password reset timeout for tests
PASSWORD_RESET_TIMEOUT = 300  # 5 minutes
