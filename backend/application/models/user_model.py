from flask import jsonify
from flask import request
from application import db
import datetime
from flask import Response
from application.response import *
import json

# =======================================================
# USER MODEL
# =======================================================	
		
class User(db.Model):
	user_id			  = db.Column(db.Integer, primary_key=True)
	user_email		   = db.Column(db.VARCHAR(255), unique=True)
	user_username		= db.Column(db.VARCHAR(255), unique=True)
	user_password		= db.Column(db.VARCHAR(255), unique=False)
	user_profile_pict	= db.Column(db.VARCHAR(255), unique=False)
	user_first_name	  = db.Column(db.VARCHAR(255), unique=False)
	user_last_name	   = db.Column(db.VARCHAR(255), unique=False)
	user_friends		 = db.Column(db.Integer, unique=False)	
	user_is_activated	= db.Column(db.Integer, unique=False)
	user_created_at	  = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	user_updated_at	  = db.Column(db.DateTime, default=datetime.datetime.utcnow)

	def __init__(
		self,
		user_email, 
		user_username, 
		user_password, 
		user_profile_pict, 
		user_first_name, 
		user_last_name, 
		user_friends, 
		user_is_activated, 
		user_created_at,
		user_updated_at 
	):
		self.user_email		 = user_email
		self.user_username	  = user_username
		self.user_password	  = user_password
		self.user_profile_pict  = user_profile_pict
		self.user_first_name	= user_first_name
		self.user_last_name	 = user_last_name	
		self.user_friends	   = user_friends
		self.user_is_activated   = user_is_activated
		self.user_created_at	= user_created_at
		self.user_updated_at	= user_updated_at

	def __repr__(self):
		return '<User %r>' % self.user_username

	# =======================================================
	# GET ALL USER
	# =======================================================	
	@staticmethod
	def getAllUsers():
		all_users = User.query.all()
		result = []
		
		for user in all_users:
			user_data = {}
			user_data['user_id'] = user.user_id
			user_data['user_email'] = user.user_email
			user_data['user_username'] = user.user_username
			user_data['user_password'] = user.user_password
			user_data['user_profile_pict'] = user.user_profile_pict
			user_data['user_first_name'] = user.user_first_name
			user_data['user_last_name'] = user.user_last_name
			user_data['user_friends'] = user.user_friends
			user_data['user_is_activated'] = user.user_is_activated
			user_data['user_created_at'] = user.user_created_at
			user_data['user_updated_at'] = user.user_updated_at
			result.append(user_data)
			
		resp_result = result
		resp_status = OK
		resp_mimetype = JSON_TYPE

		return Response(response=resp_result, status=resp_status, mimetype=resp_mimetype)

	# =======================================================
	# GET ONE USER
	# =======================================================
	@staticmethod
	def getOneUser(id):		
		all_users = User.query.all()
		output = []
		
		for user in all_users:
			user_data = {}
			user_data['user_id'] = user.user_id
			user_data['user_email'] = user.user_email
			user_data['user_username'] = user.user_username
			user_data['user_password'] = user.user_password
			user_data['user_profile_pict'] = user.user_profile_pict
			user_data['user_first_name'] = user.user_first_name
			user_data['user_last_name'] = user.user_last_name
			user_data['user_friends'] = user.user_friends
			user_data['user_is_activated'] = user.user_is_activated
			user_data['user_created_at'] = user.user_created_at
			user_data['user_updated_at'] = user.user_updated_at
			output.append(user_data)
			
			
		try:	
			user = [oneUser for oneUser in output if oneUser['user_id'] == id]
			resp_result = user[0]
			resp_status = OK
			resp_mimetype = JSON_TYPE
			print 'in'
			return Response(response=resp_result, status=resp_status, mimetype=resp_mimetype)
		except:
			return Response(status=NOT_FOUND)
			
	# =======================================================
	# POST ONE USER
	# =======================================================
	@staticmethod
	def addOneUser(input):
		new_user = User(
			input['user_email'],
			input['user_username'],
			input['user_password'],
			"no picture",
			input['user_first_name'],
			input['user_last_name'],
			0,
			0,
			datetime.datetime.now(),
			datetime.datetime.now(),
		)
		
		try:			
			db.session.add(new_user)
			db.session.commit()
			user = User.query.filter_by(user_email=input['user_email']).first()

			out = False
			while out == False:
				try:
					user = User.query.filter_by(user_email=input['user_email']).first()
					if user.user_id:
						out = True
				except:
					out = False

			location = '/user/' + str(user.user_id)
			resp_headers = { 'location' : location }
			
			return Response(status=CREATED, headers=resp_headers)
		except:
			return Response(status=CONFLICT)
		
	# =======================================================
	# REMOVE ONE USER
	# =======================================================
	@staticmethod
	def removeOneUser(user_id):

		try:
			db.session.query(User).filter_by(user_id=user_id).delete()
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
			selected_user = User.query.filter_by(user_id=id).first()
			selected_user.user_email = user['user_email']
			selected_user.user_username = user['user_username']
			selected_user.user_password = user['user_password']
			selected_user.user_profile_pict = user['user_profile_pict']
			selected_user.user_first_name = user['user_first_name']
			selected_user.user_last_name = user['user_last_name']
			selected_user.user_is_activated = user['user_is_activated']
			selected_user.user_created_at = selected_user.user_created_at
			selected_user.user_updated_at = datetime.datetime.now()
			
			db.session.merge(selected_user)
			db.session.commit()
			
			return Response(status=OK)
		except:
			return Response(status=CONFLICT)
