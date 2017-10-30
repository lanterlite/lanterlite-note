from application.models.user_model import User
from application import app
from application.response import *
from application.settings import *

from flasgger import swag_from

from flask import jsonify
from flask import request
from flask import Response

from math import ceil

import json
import hashlib

@app.route(BACKEND_VERSION + USER_ROUTE, methods=['GET'])
def getAll():
	output = User.getAll()
	resp_result = output.response
	resp_status = OK
	return json.dumps(resp_result), resp_status

@app.route(BACKEND_VERSION + USER_ROUTE + '/<int:id>', methods=['GET'])
def getOne(id):
	output = User.getOne(id)
	if str(OK) in str(output.status):
		resp_result = output.response
		resp_status = OK
		return json.dumps(resp_result), resp_status
	else:
		return output

@app.route(BACKEND_VERSION + USER_ROUTE, methods=['POST'])
def addOne():	
	output = User.addOne(request.json)
	return output

@app.route(BACKEND_VERSION + USER_ROUTE, methods=['PUT'])
def upsertSome():
	output = User.upsertSome(request.json)
	return output
	
@app.route(BACKEND_VERSION + USER_ROUTE + '/upload/', methods=['POST'])
def uploadImage():
	output = User.uploadImage(request)
	if str(OK) in str(output.status):
		all_users = User.getAll()
		uploader = filter(lambda user: str(user['id']).find(str(request.headers['id'])) != -1 , all_users.response)
		uploader[0]['image'] = output.response['filename']
		output = User.upsertSome(uploader)
	return output

@app.route(BACKEND_VERSION + USER_ROUTE + '/image/', methods=['put'])
def getImage():
	print 'b'
	output = User.getImage(request)
	return output

	# f = open('/Users/Desktop/febROSTER2012.xls')
 	# return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

# @app.route(BACKEND_VERSION + USER_ROUTE + '/<int:id>', methods=['PUT'])
# def editOne_user(id):
# 	output = User.getOneUser(id)
# 	if str(OK) in str(output.status):
# 		output = User.editOneUser(id, request.json)
# 		if str(OK) in str(output.status):
# 			user = User.getOneUser(request.json['updated_by'])
# 			if str(OK) in str(user.status):
# 				action = {}
# 				action['action'] = 'User: ' + user.response['first_name'] + ' has updated user: ' + request.json['first_name']
# 				log = ActivityLog.addOneLog(action)
# 				return output
# 			else:
# 				return user
# 		else:
# 			return output
# 	else:
# 		return output
		
# @app.route(BACKEND_VERSION + USER_ROUTE + '/<int:id>', methods=['DELETE'])
# def removeOne_user(id):
# 	if request.headers['User-Type'] == UserType.SUPERADMIN.name:
# 		user = User.getOneUser(id)
# 		if str(OK) in str(user.status):
# 			output = User.removeOneUser(id)
# 			if str(OK) in str(output.status):
# 				action = {}
# 				action['action'] = 'User: ' + user.response['first_name'] + ' has deleted'
# 				log = ActivityLog.addOneLog(action)		
# 			return output
# 		else:
# 			return user
# 	else:
# 		return Response(status=METHOD_NOT_ALLOWED)

# @app.route(BACKEND_VERSION + USER_ROUTE + '/login/validation', methods=['POST'])
# def validateOne_user():
# 	print request.json
# 	all_users = User.getAllUser()
# 	filteredRes = filter(lambda user: user['email'].lower().find(request.json['email'].lower()) != -1 , all_users.response)
# 	hashedInputPassword = hashlib.md5(request.json['password']).hexdigest()
# 	hashedSavedPassword = filteredRes[0]['password']
# 	print str(hashedInputPassword)
# 	print str(hashedSavedPassword)
# 	if str(hashedInputPassword) in str(hashedSavedPassword):
# 		print str(hashedInputPassword)
# 		resp_status = OK
# 		return json.dumps(filteredRes[0]), resp_status
# 	else:
# 		return Response(status=NOT_ACCEPTABLE)

