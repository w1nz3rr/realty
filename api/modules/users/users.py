from flask import Blueprint, jsonify
from api.apiclass.UserAPI import UserAPI
from api.modules.auth.jwt_token import *

users = Blueprint('users', __name__, url_prefix='/api/users')

@jwt_required()
@users.get('/<user_id>')
def get_user(user_id):
    userAPI = UserAPI()
    response = userAPI.get_user(user_id)
    if response == 'user not in db':
        return jsonify(error=response)
    else:
        return jsonify(user=response)

