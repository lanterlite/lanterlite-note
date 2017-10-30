from application import db
from application import app
from application.response import *
from application.settings import *

from flask import Response
from flask import request
from flask import send_from_directory

import datetime
import hashlib
import os
import json
from PIL import Image
import base64
import cStringIO
import dateutil.parser

# =======================================================
# USER MODEL
# =======================================================	

class User(db.Model):
	id				= db.Column(db.Integer, primary_key=True)
	name			= db.Column(db.VARCHAR(255), unique=False)
	email			= db.Column(db.VARCHAR(255), unique=True)
	password		= db.Column(db.VARCHAR(255), unique=False)
	username		= db.Column(db.VARCHAR(255), unique=True)
	image			= db.Column(db.VARCHAR, unique=False)
	friendlist		= db.Column(db.ARRAY(db.Integer, as_tuple=False, dimensions=None, zero_indexes=False))
	is_activated	= db.Column(db.Boolean, unique=False, default=False)
	created_at	  	= db.Column(db.DateTime, default=datetime.datetime.utcnow)
	updated_at	  	= db.Column(db.DateTime, default=datetime.datetime.utcnow)
	violation_id 	= db.Column(db.Integer, db.ForeignKey('violation.id'), nullable=True, unique=False)

	def __init__( self, name, email, password, username, image, friendlist, is_activated, created_at, updated_at, violation_id ):
		self.name			= name
		self.email			= email
		self.password		= password
		self.username		= username
		self.image  		= image
		self.friendlist	   	= friendlist
		self.is_activated   = is_activated
		self.created_at		= created_at.isoformat()
		self.updated_at		= updated_at.isoformat()
		self.violation_id	= violation_id

	def __repr__(self):
		return '<User %r>' % self.username

	# =======================================================
	# GET ALL USER
	# =======================================================	
	@staticmethod
	def getAll():
		all_users = User.query.all()
		result = []
		
		for user in all_users:
			data = {}
			data['id'] = user.id
			data['name'] = user.name
			data['email'] = user.email
			data['password'] = user.password
			data['username'] = user.username
			data['image'] = user.image
			data['friendlist'] = user.friendlist
			data['is_activated'] = user.is_activated
			data['created_at'] = user.created_at.isoformat()
			data['updated_at'] = user.updated_at.isoformat()
			data['violation_id'] = user.violation_id
			result.append(data)
			
		resp_result = result
		resp_status = OK
		resp_mimetype = JSON_TYPE

		return Response(response=resp_result, status=resp_status, mimetype=resp_mimetype)

	# =======================================================
	# GET ONE USER
	# =======================================================
	@staticmethod
	def getOne(id):		
		all_users = User.query.all()
		output = []
		
		for user in all_users:
			data = {}
			data['id'] = user.id
			data['name'] = user.name
			data['email'] = user.email
			data['password'] = user.password
			data['username'] = user.username
			data['image'] = user.image
			data['friendlist'] = user.friendlist
			data['is_activated'] = user.is_activated
			data['created_at'] = user.created_at.isoformat()
			data['updated_at'] = user.updated_at.isoformat()
			data['violation_id'] = user.violation_id
			output.append(data)			
			
		try:	
			user = [oneUser for oneUser in output if oneUser['id'] == id]
			resp_result = user[0]
			resp_status = OK
			resp_mimetype = JSON_TYPE
			return Response(response=resp_result, status=resp_status, mimetype=resp_mimetype)
		except:
			return Response(status=NOT_FOUND)
			
	# =======================================================
	# POST ONE USER
	# =======================================================
	@staticmethod
	def addOne(input):
		new_user = User(
			input['name'],
			input['email'],
			input['password'],
			input['username'],
			input['image'],
			input['friendlist'],
			input['is_activated'],
			datetime.datetime.now(),
			datetime.datetime.now(),
			input['violation_id'],
		)
		
		try:			
			db.session.add(new_user)
			db.session.commit()
			created_date = datetime.datetime.now()
			created_year = created_date.strftime("%Y")
			created_month = created_date.strftime("%m")
			created_day = created_date.strftime("%d")

			private_path = 'private/'
			account_path = private_path + 'account/'
			year_path = account_path + created_year + '/'
			month_path = year_path + created_month + '/'
			day_path = month_path + created_day + '/'

			full_path = day_path + request.headers['id'] + '/'

			if not os.path.isdir(os.path.abspath(private_path)):
				os.mkdir(os.path.abspath(private_path))
			if not os.path.isdir(os.path.abspath(account_path)):
				os.mkdir(os.path.abspath(account_path))
			if not os.path.isdir(os.path.abspath(year_path)):
				os.mkdir(os.path.abspath(year_path))
			if not os.path.isdir(os.path.abspath(month_path)):
				os.mkdir(os.path.abspath(month_path))
			if not os.path.isdir(os.path.abspath(day_path)):
				os.mkdir(os.path.abspath(day_path))
			if not os.path.isdir(os.path.abspath(full_path)):
				os.mkdir(os.path.abspath(full_path))
			return Response(status=CREATED)
		except:
			return Response(status=CONFLICT)
		
	# =======================================================
	# REMOVE ONE USER
	# =======================================================
	@staticmethod
	def removeOneUser(id):
		try:
			db.session.query(User).filter_by(id=id).delete()
			db.session.commit()
			return Response(status=OK)
		except:
			return Response(status=CONFLICT)
		
	# =======================================================
	# EDIT ONE USER
	# =======================================================
	@staticmethod
	def editOneUser(id, user):
		try:
			selected_user = User.query.filter_by(id=id).first()
			selected_user.name = user['name']
			selected_user.email = user['email']
			selected_user.password = user['password']
			selected_user.username = user['username']
			selected_user.image = user['image']
			selected_user.is_activated = user['is_activated']
			selected_user.created_at = selected_user.created_at
			selected_user.updated_at = datetime.datetime.now()
			selected_user.violation_id = user['violation_id']
			
			db.session.merge(selected_user)
			db.session.commit()
			
			return Response(status=OK)
		except:
			return Response(status=CONFLICT)

	# =======================================================
	# MERGE ONE USER
	# =======================================================	
	@staticmethod
	def upsertSome(input):
		all_data = User.query.all()
		output = []
		for data in all_data:
			output.append(data)
		merge_index_list = []
		i = 0
		for j in range(0, len(input)):
			try:
				data_list = 0
				try:
					data_list = [oneUser for oneUser in output if oneUser.id == input[i]['id']]
				except:
					print 'data not exist 1'
				password = None
				newPassword = hashlib.md5(input[i]['password']).hexdigest()
				if data_list[0].password == newPassword or data_list[0].password == input[i]['password']:
					password = data_list[0].password
				elif data_list[0].password != newPassword or data_list[0].password !=  input[i]['password']:
					password = newPassword
				data_list[0].name 			= input[i]['name']
				data_list[0].email 			= input[i]['email']
				data_list[0].password 		= password
				data_list[0].username 		= input[i]['username']
				data_list[0].image 			= input[i]['image']
				data_list[0].friendlist 	= input[i]['friendlist']
				data_list[0].is_activated 	= input[i]['is_activated']
				data_list[0].created_at 	= input[i]['created_at']
				data_list[0].updated_at 	= input[i]['updated_at']
				data_list[0].violation_id 	= input[i]['violation_id']
				db.session.merge(data_list[0])
				input.pop(i)
				i = i - 1
			except:
				print 'data not exist 2'
			i = i + 1
			
		db.session.commit()
		# objects = []
		# for i in range(0, len(input)):
		# 	newPassword = hashlib.md5(input[i]['password']).hexdigest()
		# 	data = User(
		# 		input[i]['name'],
		# 		input[i]['email'],
		# 		newPassword,
		# 		input[i]['username'],
		# 		input[i]['image'],
		# 		input[i]['friendlist'],
		# 		input[i]['is_activated'],
		# 		datetime.datetime.now(),
		# 		datetime.datetime.now(),
		# 		input[i]['violation_id'],
		# 	)
		# 	objects.append(data)

		# engine = create_engine(SQLALCHEMY_DATABASE_URI)
		# Session = sessionmaker(bind = engine)
		# session = Session()
		# session.bulk_save_objects(objects)		
		# session.commit()
		
		return Response(status=OK)

	@staticmethod
	def getImage(request):
		created_date = dateutil.parser.parse(request.headers['created_at'])
		created_year = created_date.strftime("%Y")
		created_month = created_date.strftime("%m")
		created_day = created_date.strftime("%d")

		private_path = 'private/'
		account_path = private_path + 'account/'
		year_path = account_path + created_year + '/'
		month_path = year_path + created_month + '/'
		day_path = month_path + created_day + '/'

		full_path = day_path + request.headers['id'] + '/' + request.headers['filename']
		size = 128, 128
		jpgfile = Image.open(full_path)
		# jpgfile.thumbnail(size) # file size jadi lebih kecil tapi gambar jadi pecah
		buffer = cStringIO.StringIO()
		jpgfile = jpgfile.convert("RGB")
		jpgfile.save(buffer, format="JPEG")
		jpgfile_data = buffer.getvalue()
		data_url = 'data:image/jpg;base64,' + base64.b64encode(jpgfile_data)
		return data_url

	@staticmethod
	def uploadImage(request):
		created_date = dateutil.parser.parse(request.headers['created_at'])
		created_year = created_date.strftime("%Y")
		created_month = created_date.strftime("%m")
		created_day = created_date.strftime("%d")

		private_path = 'private/'
		account_path = private_path + 'account/'
		year_path = account_path + created_year + '/'
		month_path = year_path + created_month + '/'
		day_path = month_path + created_day + '/'

		full_path = day_path + request.headers['id'] + '/'

		if not os.path.isdir(os.path.abspath(private_path)):
			os.mkdir(os.path.abspath(private_path))
		if not os.path.isdir(os.path.abspath(account_path)):
			os.mkdir(os.path.abspath(account_path))
		if not os.path.isdir(os.path.abspath(year_path)):
			os.mkdir(os.path.abspath(year_path))
		if not os.path.isdir(os.path.abspath(month_path)):
			os.mkdir(os.path.abspath(month_path))
		if not os.path.isdir(os.path.abspath(day_path)):
			os.mkdir(os.path.abspath(day_path))
		if not os.path.isdir(os.path.abspath(full_path)):
			os.mkdir(os.path.abspath(full_path))

		year = datetime.datetime.now().strftime("%Y")
		month = datetime.datetime.now().strftime("%m")
		day = datetime.datetime.now().strftime("%d")

		hour = datetime.datetime.now().strftime("%H")
		minute = datetime.datetime.now().strftime("%M")
		second = datetime.datetime.now().strftime("%S")

		resp_result = None
		resp_mimetype = JSON_TYPE
		for file in request.files.getlist("data"):
			print file
			# if file and allowed_file(file.filename):
			filename = 'IMG' + year + month + day + hour + minute + second + '.jpg'
			destination = "/".join([full_path, filename])
			file.save(destination)
							
			resp_result = {'filename': filename, 'path': full_path}
			# resp_result = json.dumps(resp_result)
			resp_status = OK
			resp_mimetype = JSON_TYPE
			
			return Response(response=resp_result, status=OK, mimetype=resp_mimetype)		
		return Response(status=NOT_FOUND, mimetype=resp_mimetype)		

# For a given file, return whether it's an allowed type or not
# =======================================================
# ALLOWED FILES
# =======================================================
def allowed_file(filename):
	return '.' in filename and \
		 filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

