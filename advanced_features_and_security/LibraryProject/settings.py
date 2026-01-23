INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'relationship_app',
]

LOGIN_REDIRECT_URL = "/books/"
LOGOUT_REDIRECT_URL = "/login/"
LOGIN_URL = "/login/"
# Use the custom user model
AUTH_USER_MODEL = "bookshelf.CustomUser"



MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

