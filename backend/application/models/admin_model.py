from application import db
from application.response import *

from flask import Response

import datetime

# =======================================================
# PAPER MODEL
# =======================================================	
		
class Admin(db.Model):
	id			= db.Column(db.Integer, primary_key=True)
	name		= db.Column(db.VARCHAR(255), unique=False)
	email		= db.Column(db.VARCHAR(255), unique=True)
	password	= db.Column(db.VARCHAR(255), unique=False)
	is_enabled	= db.Column(db.Boolean, unique=False, default=True)
	created_at	= db.Column(db.DateTime, default=datetime.datetime.utcnow)
	updated_at	= db.Column(db.DateTime, default=datetime.datetime.utcnow)
	created_by	= db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False, unique=False)
	updated_by	= db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False, unique=False)

	def __init__( self, name, email, password, is_enabled, created_at, updated_at, created_by, updated_by ):
		self.name		= name
		self.email		= email
		self.password	= password
		self.is_enabled	= is_enabled
		self.created_at	= created_at
		self.updated_at	= updated_at
		self.created_by	= created_by
		self.updated_by	= updated_by

	def __repr__(self):
		return '<Admin %r>' % self.title

	# =======================================================
	# GET ALL DATA
	# =======================================================	
	@staticmethod
	def getAll():
		all_data = Admin.query.all()
		result = []
		
		for _data in all_data:
			data = {}
			data['id'] = _data.id
			data['title'] = _data.title
			data['created_at'] = _data.created_at
			data['updated_at'] = _data.updated_at
			data['user_id'] = _data.user_id
			result.append(data)
			
		resp_result = result
		resp_status = OK
		resp_mimetype = JSON_TYPE

		return Response(response=resp_result, status=resp_status, mimetype=resp_mimetype)

	# =======================================================
	# GET ONE DATA
	# =======================================================
	@staticmethod
	def getOne(id):		
		all_data = Admin.query.all()
		output = []
		
		for _data in all_data:
			data = {}
			data['id'] = _data.id
			data['title'] = _data.name
			data['created_at'] = _data.created_at
			data['updated_at'] = _data.updated_at
			data['user_id'] = _data.user_id
			output.append(data)			
			
		try:	
			data = [oneData for oneData in output if oneData['id'] == id]
			resp_result = data[0]
			resp_status = OK
			resp_mimetype = JSON_TYPE
			return Response(response=resp_result, status=resp_status, mimetype=resp_mimetype)
		except:
			return Response(status=NOT_FOUND)
			
	# =======================================================
	# POST ONE DATA
	# =======================================================
	@staticmethod
	def addOne(input):
		new_data = Admin(
			input['title'],
			datetime.datetime.now(),
			datetime.datetime.now(),
			input['user_id'],
		)
		
		try:			
			db.session.add(new_data)
			db.session.commit()
			data = Admin.query.filter_by(id=input['user_id']).first()

			return Response(status=CREATED, headers=resp_headers)
		except:
			return Response(status=CONFLICT)
		
	# =======================================================
	# REMOVE ONE DATA
	# =======================================================
	@staticmethod
	def removeOne(id):
		try:
			db.session.query(Admin).filter_by(id=id).delete()
			db.session.commit()
			return Response(status=OK)
		except:
			return Response(status=CONFLICT)
		
	# =======================================================
	# EDIT ONE DATA
	# =======================================================
	@staticmethod
	def editOne(id, input):
		try:
			selected_user = Admin.query.filter_by(id=id).first()
			selected_user.title = input['title']
			selected_user.created_at = selected_user.created_at
			selected_user.updated_at = datetime.datetime.now()
			selected_user.user_id = input['user_id']
			
			db.session.merge(selected_user)
			db.session.commit()
			
			return Response(status=OK)
		except:
			return Response(status=CONFLICT)
