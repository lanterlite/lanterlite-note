from application import db
from application.response import *

from flask import Response

import datetime

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
	is_activated	= db.Column(db.Boolean, unique=False, default=True)
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
	def getAllUsers():
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
	def addOneUser(input):
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
			user = User.query.filter_by(email=input['email']).first()

			return Response(status=CREATED, headers=resp_headers)
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
