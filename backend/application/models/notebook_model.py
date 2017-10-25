from application import db
from application.response import *

from flask import Response

import datetime

# =======================================================
# NOTEBOOK MODEL
# =======================================================	
		
class Notebook(db.Model):
	id			= db.Column(db.Integer, primary_key=True)
	title		= db.Column(db.VARCHAR, unique=False)
	created_at	= db.Column(db.DateTime, default=datetime.datetime.utcnow)
	updated_at	= db.Column(db.DateTime, default=datetime.datetime.utcnow)
	user_id		= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=False)

	def __init__( self, title, created_at, updated_at, user_id ):
		self.title		= title
		self.created_at	= created_at
		self.updated_at	= updated_at
		self.user_id	= user_id

	def __repr__(self):
		return '<Notebook %r>' % self.title

	# =======================================================
	# GET ALL DATA
	# =======================================================	
	@staticmethod
	def getAll():
		all_data = Notebook.query.all()
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
		all_data = Notebook.query.all()
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
		new_data = Notebook(
			input['title'],
			datetime.datetime.now(),
			datetime.datetime.now(),
			input['user_id'],
		)
		
		try:			
			db.session.add(new_data)
			db.session.commit()
			data = Notebook.query.filter_by(id=input['user_id']).first()

			return Response(status=CREATED, headers=resp_headers)
		except:
			return Response(status=CONFLICT)
		
	# =======================================================
	# REMOVE ONE DATA
	# =======================================================
	@staticmethod
	def removeOne(id):
		try:
			db.session.query(Notebook).filter_by(id=id).delete()
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
			selected_user = Notebook.query.filter_by(id=id).first()
			selected_user.title = input['title']
			selected_user.created_at = selected_user.created_at
			selected_user.updated_at = datetime.datetime.now()
			selected_user.user_id = input['user_id']
			
			db.session.merge(selected_user)
			db.session.commit()
			
			return Response(status=OK)
		except:
			return Response(status=CONFLICT)
