# =========================
# SECURITY CONFIGURATIONS
# =========================

# Turn off debug in production
DEBUG = False

# Browser-level protections
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Cookie security (HTTPS only)
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
