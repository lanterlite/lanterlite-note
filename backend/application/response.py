# Define custom error messages here
from flask import Response
# from flask import make_response
NOT_FOUND 						= 404
METHOD_NOT_ALLOWED 				= 405
FORBIDDEN		 				= 403
NOT_ACCEPTABLE 					= 406
PROXY_AUTHENTICATION_REQUIRED 	= 407
REQUEST_TIMEOUT 				= 408
CONFLICT 						= 409

OK 								= 200
CREATED 						= 201
ACCEPTED 						= 202
NO_CONTENT 						= 204

PERMISSION_DENIED				= 550

JSON_TYPE						= "application/json"

LOG_NOT_EXIST 		= Response(response={"message": "Log does not exists"}, status=NOT_FOUND, mimetype='application/json')
LOG_CONFLICT 		= Response(response={"message": "Log conflict"}, status=CONFLICT, mimetype='application/json')

USER_NOT_EXIST 		= Response(status=NOT_FOUND)
USER_CONFLICT 		= Response(response={"message": "User conflict"}, status=CONFLICT, mimetype='application/json')

CANDIDATE_NOT_EXIST = Response(response={"message": "Candidate does not exists"}, status=NOT_FOUND, mimetype='application/json')
CANDIDATE_CONFLICT 	= Response(response={"message": "Candidate conflict"}, status=CONFLICT, mimetype='application/json')

RESUME_NOT_EXIST 	= Response(response={"message": "Resume does not exists"}, status=NOT_FOUND, mimetype='application/json')
RESUME_CONFLICT 	= Response(response={"message": "Resume conflict"}, status=CONFLICT, mimetype='application/json')


# LOG_NOT_EXIST = make_response('{"message": "Log does not exists"}')
# LOG_NOT_EXIST.status_code = 404
# LOG_NOT_EXIST.mimetype = 'application/json'

# LOG_CONFLICT = make_response('{"message": "Log conflict"}')
# LOG_CONFLICT.status_code = 409
# LOG_CONFLICT.mimetype = 'application/json'

# EMAIL_IN_USE = ({'message': 'User with that email already exists'}, 409)
# UNAUTHORIZED = ({'message': 'Authentication is required to access this resource'}, 401)
# BAD_CREDENTIALS = ({'message': 'Invalid credentials'}, 401)
# FORBIDDEN = ({'message': 'Access to this resource is forbidden'}, 403)
# CODE_NOT_VALID = ({'message': 'Valid code is required to reset a password'}, 401)
# TOO_MANY_REQUESTS = ({'message': 'Too many requests'}, 429)
