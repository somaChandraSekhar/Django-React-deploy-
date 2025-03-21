import os
from .settings import *
from .settings import BASE_DIR



ALLOWED_HOSTS =[os.environ['WEBSITE_HOSTNAME']]

CSRF_TRUSTED_ORIGINS =['https://'+os.environ['WEBSITE_HOSTNAME']]
DEBUG=False

SECRET_KEY=os.environ['MY_SECRET_KEY']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
    'corsheaders.middleware.CorsMiddleware',  # Add this
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ALLOWED_ORIGINS = [

# ]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"
,
    },
}
CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']

# Parse the connection string
params = dict(pair.split('=') for pair in CONNECTION.split(' ') if '=' in pair)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": params['dbname'],
        "USER": params['user'],
        "PASSWORD": params['password'],
        "HOST": params['host'],
        "OPTIONS": {"sslmode": "require"},  # Ensure SSL is enabled
    }
}

STATIC_ROOT = BASE_DIR/'staticfiles'