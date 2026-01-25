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

# ============================
# HTTPS & Security Settings
# ============================

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
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
