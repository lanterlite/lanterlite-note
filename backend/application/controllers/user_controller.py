from flasgger import swag_from

from flask import jsonify
from flask import request

from application.models.user_model import User

from application import app
from application.response import *
from flask import Response
import json

@app.route('/user', methods=['GET'])
@swag_from('../swagger/user/user_get_all.yml')
def getAll_user():
	output = User.getAllUsers()
	result = output.response
	return jsonify({'result' : result})

@app.route('/user/<int:user_id>', methods=['GET'])
@swag_from('../swagger/user/user_get_one.yml')
def getOne_user(user_id):
	output = User.getOneUser(user_id)
	if str(OK) in str(output.status):
		result = output.response
		return jsonify({'result' : result})
	else:
		return output

@app.route('/user', methods=['POST'])
@swag_from('../swagger/user/user_add_one.yml')
def addOne_user():	
	output = User.addOneUser(request.json)
	return output

@app.route('/user/<int:user_id>', methods=['PUT'])
@swag_from('../swagger/user/user_edit_one.yml')
def editOne_user(user_id):
	output = User.getOneUser(user_id)
	if str(OK) in str(output.status):
		output = User.editOneUser(user_id, request.json)
		return output
	else:
		return output
		
@app.route('/user/<int:user_id>', methods=['DELETE'])
@swag_from('../swagger/user/user_remove_one.yml')
def removeOne_user(user_id):
	user = User.getOneUser(user_id)
	if str(OK) in str(user.status):
		output = User.removeOneUser(user_id)
		return output
	else:
		return user
