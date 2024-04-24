from flask import Blueprint, jsonify, request
from api.apiclass.UserAPI import UserAPI
from api.modules.auth.jwt_token import *

blacklist = Blueprint('blacklist', __name__, url_prefix='/api/users/<int:user_id>/blacklist')

@jwt_required()
@blacklist.post('/')
def post_blacklist(user_id):
    userAPI = UserAPI()
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    response = userAPI.post_blacklist(self_id, user_id)
    if response == 'user in blacklist':
        return jsonify(error='user in blacklist')
    else:
        return jsonify(status='ok')

@jwt_required()
@blacklist.delete('/')
def delete_blacklist(user_id):
    userAPI = UserAPI()
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    response = userAPI.delete_blacklist(self_id, user_id)
    if response == 'user not in blacklist':
        return jsonify(error='user not in blacklist')
    else:
        return jsonify(status='ok')