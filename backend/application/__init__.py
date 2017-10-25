from flask import Flask
from settings import DEBUG
# from settings import *
from settings import SQLALCHEMY_DATABASE_URI
# from application.settings import *

app = Flask(__name__)
# app = Flask(__name__, static_url_path='')

app.debug = DEBUG
# app.config.from_object('settings')
app.config.from_pyfile('settings.py')

# app.static_folder = 'static'
# from flask import request
# import os

# =============================================
# FLASK SQLALCHEMY
# =============================================
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

# =============================================
# FLASK SWAGGER
# =============================================
from flasgger import Swagger
swagger = Swagger(app)

# =============================================
# FLASK CORS
# =============================================
from flask_cors import CORS, cross_origin
CORS(app)
cors = CORS(app, resoureces={r"http://localhost:5000": {"origins": "*"}})

# =============================================
# ROUTES-MODELS-CONTROLLERS
# =============================================
import models
import routes
import controllers



@app.url_defaults
def hashed_static_file(endpoint, values):
	if 'static' == endpoint or endpoint.endswith('.static'):
		filename = values.get('filename')
		if filename:
			blueprint = request.blueprint
			if '.' in endpoint:  # blueprint
				blueprint = endpoint.rsplit('.', 1)[0]

			static_folder = app.static_folder
		   # use blueprint, but dont set `static_folder` option
			if blueprint and app.blueprints[blueprint].static_folder:
				static_folder = app.blueprints[blueprint].static_folder

			fp = os.path.join(static_folder, filename)
			if os.path.exists(fp):
				values['_'] = int(os.stat(fp).st_mtime)
				