import os

# =====================================================
# FLASK CORE SETTINGS 
# =====================================================
DEBUG = True
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')

PORT = os.getenv('PORT', 5000)

# =====================================================
# FLASK POSTGRES SETTINGS 
# =====================================================
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/lanternoteDB'
	
# =====================================================
# FLASK LOG SETTINGS 
# =====================================================
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])








# SECRET_KEY = os.getenv('SECRET_KEY', None)
# assert SECRET_KEY

# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
    # 'postgres://docker:docker@{0}/docker'.format(os.getenv('DB_1_PORT_5432_TCP_ADDR')))


# TESTING = False
# SECRET_KEY = 'qh\x98\xc4o\xc4]\x8f\x8d\x93\xa4\xec\xc5\xfd]\xf8\xb1c\x84\x86\xa7A\xcb\xc0'
# PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 30

# flask wtf settings
# WTF_CSRF_ENABLED = True

# flask mongoengine settings
# MONGODB_SETTINGS = {
    # 'DB': 'flaskexample'
# }

# flask mail settings
# MAIL_DEFAULT_SENDER = 'noreply@yourmail.com'

# project settings
# PROJECT_PASSWORD_HASH_METHOD = 'pbkdf2:sha1'
# PROJECT_SITE_NAME = u'Flask Example'
# PROJECT_SITE_URL = u'http://127.0.0.1:5000'
# PROJECT_SIGNUP_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds
# PROJECT_RECOVER_PASSWORD_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds