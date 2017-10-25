from application import db
from application.response import *

from flask import Response

import datetime

# =======================================================
# PAPER MODEL
# =======================================================	
		
class Paper(db.Model):
	id				= db.Column(db.Integer, primary_key=True)
	text			= db.Column(db.VARCHAR, unique=False)
	is_pinned		= db.Column(db.Boolean, unique=False, default=False)
	page			= db.Column(db.Integer, unique=False)
	created_at	  	= db.Column(db.DateTime, default=datetime.datetime.utcnow)
	updated_at	  	= db.Column(db.DateTime, default=datetime.datetime.utcnow)
	notebook_id		= db.Column(db.Integer, db.ForeignKey('notebook.id'), nullable=False, unique=False)

	def __init__( self, text, is_pinned, created_at, updated_at, notebook_id ):
		self.text			= text
		self.is_pinned		= is_pinned
		self.created_at		= created_at
		self.updated_at		= updated_at
		self.notebook_id	= notebook_id

	def __repr__(self):
		return '<Paper %r>' % self.page

