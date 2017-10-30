import os

# =====================================================
# CORE SETTINGS
# =====================================================
DEBUG = True
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')

PORT = os.getenv('PORT', 5000)

# =====================================================
# POSTGRES SETTINGS 
# =====================================================
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/lanternoteDB'

# =====================================================
# FLASK UPLOAD FILE SETTINGS 
# =====================================================
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# =====================================================
# URL SETTINGS 
# =====================================================
SITE_URL = 'localhost:5000' #http://localhost:5000

BACKEND_VERSION = '/v1'
USER_ROUTE = '/user'
ADMIN_ROUTE = '/admin'
NOTEBOOK_ROUTE = '/notebook'
PAPER_ROUTE = '/paper'
VALIDATION_ROUTE = '/validation'