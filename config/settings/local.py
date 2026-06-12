from .base import *

DEBUG = True
print(os.getenv('POSTGRES_DB'),"oss")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'PASSWORD':os.getenv('POSTGRES_PASSWORD'),
        'USER':os.getenv('POSTGRES_USER'),
        'HOST':os.getenv('DB_HOST'),
        'PORT':os.getenv('DB_PORT')

    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "127.0.0.1"
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL') 