from flask import Blueprint, jsonify, request
from api.DB.db import DB
from api.modules.auth.jwt_token import *

complaints = Blueprint('complaints ', __name__, url_prefix='/api/users/<int:user_id>/complaints')
db = DB()

@jwt_required()
@complaints.get('/')
def get_complaints(user_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    procedure = f'exec get_complaints {self_id}, {user_id}'
    response = db.execute_procedure(procedure)[0]
    if response[0] == 'no complaints':
        return jsonify(error=response[0])
    data = {'complaints_id': response[0], 'self_id': response[1], 'user_id': response[2],
            'reason': response[3], 'description': response[4], 'create_at': response[5]}
    return jsonify(complaints=data)


@jwt_required()
@complaints.post('/')
def post_complaints(user_id):
    reason = request.json.get('reason')
    description = request.json.get('description')
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    procedure = f'exec post_complaints {self_id}, {user_id}, {reason}, {description}'
    response = db.execute_procedure(procedure)[0]
    if response[0] == 'complaints in db':
        return jsonify(error=response[0])
    data = {'complaints_id': response[0], 'self_id': response[1], 'user_id': response[2],
            'reason': response[3], 'description': response[4], 'create_at': response[5]}
    return jsonify(complaints=data)