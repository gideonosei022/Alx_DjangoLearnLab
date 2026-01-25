INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'relationship_app',
]


# Use the custom user model
AUTH_USER_MODEL = "bookshelf.CustomUser"

LOGIN_REDIRECT_URL = "/books/"
LOGOUT_REDIRECT_URL = "/login/"
LOGIN_URL = "/login/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# SECURITY SETTINGS

# Prevent cross-site scripting (XSS) attacks in supported browsers
SECURE_BROWSER_XSS_FILTER = True

# Prevent your site from being rendered in a frame (clickjacking protection)
X_FRAME_OPTIONS = 'DENY'

# Prevent the browser from guessing content types incorrectly
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensure CSRF cookie is only sent over HTTPS
CSRF_COOKIE_SECURE = True

# Ensure session cookie is only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Set DEBUG=False in production (already recommended)
DEBUG = False

# ============================
# HTTPS & Security Settings
# ============================

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
# Forces browsers to access the site only via HTTPS for 1 year
SECURE_HSTS_SECONDS = 31536000

# Apply HSTS policy to all subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow the site to be included in browser HSTS preload lists
SECURE_HSTS_PRELOAD = True

# ============================
# Secure Cookie Settings
# ============================

# Session cookies only sent over HTTPS
SESSION_COOKIE_SECURE = True

# CSRF cookies only sent over HTTPS
CSRF_COOKIE_SECURE = True


# ============================
# Security Headers
# ============================

# Prevent clickjacking
X_FRAME_OPTIONS = "DENY"

# Prevent MIME-type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser XSS filtering
SECURE_BROWSER_XSS_FILTER = True
