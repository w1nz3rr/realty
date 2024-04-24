from flask import Blueprint, jsonify, request
from api.DB.db import DB
from api.modules.auth.jwt_token import *

blacklist = Blueprint('blacklist', __name__, url_prefix='/api/users/<int:user_id>/blacklist')
db = DB()

@jwt_required()
@blacklist.post('/')
def post_blacklist(user_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    procedure = f'exec post_blacklist {self_id}, {user_id}'
    result = db.execute_procedure(procedure)[0]
    if result[0] == 'user in blacklist':
        return jsonify(error='user in blacklist')
    else:
        return jsonify(status='ok')

@jwt_required()
@blacklist.delete('/')
def delete_blacklist(user_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    procedure = f'exec delete_blacklist {self_id}, {user_id}'
    result = db.execute_procedure(procedure)[0]
    if result[0] == 'user not in blacklist':
        return jsonify(error='user not in blacklist')
    else:
        return jsonify(status='ok')


