from application import db
from application.response import *

from flask import Response

import datetime

# =======================================================
# VIOLATION MODEL
# =======================================================	
		
class Violation(db.Model):
	id				= db.Column(db.Integer, primary_key=True)
	desc			= db.Column(db.VARCHAR(255), unique=False)
	created_at	  	= db.Column(db.DateTime, default=datetime.datetime.utcnow)
	updated_at	  	= db.Column(db.DateTime, default=datetime.datetime.utcnow)

	def __init__( self, desc, created_at, updated_at ):
		self.desc			= desc
		self.created_at		= created_at
		self.updated_at		= updated_at

	def __repr__(self):
		return '<Violation %r>' % self.desc

