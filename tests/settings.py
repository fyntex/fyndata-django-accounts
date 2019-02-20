import django  # noqa: F401

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "^e8thszumk=vywe=-9!6aizo^+h*rf2v8$88*_*@^194&-^3)n"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': 5432,
        'NAME': 'accounts_dev',
        'USER': 'django_dev',
        'PASSWORD': 'django_dev',
        'ATOMIC_REQUESTS': False,
        'AUTOCOMMIT': True,
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "fd_dj_accounts",
]

SITE_ID = 1

MIDDLEWARE = ()
