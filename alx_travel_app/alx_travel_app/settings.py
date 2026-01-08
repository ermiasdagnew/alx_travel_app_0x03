# Django settings for alx_travel_app

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django_celery_results",
    "listings",
]

# Celery configuration
CELERY_BROKER_URL = "amqp://localhost"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_BACKEND = "django-db"

# Email configuration
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "no-reply@alxtravel.com"
