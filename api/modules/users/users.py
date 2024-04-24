from flask import Blueprint, jsonify
from api.modules.auth.jwt_token import *
from api.DB.db import DB

users = Blueprint('users', __name__, url_prefix='/api/users')
db = DB()

@users.get('/<user_id>')
def get_user(user_id):
    procedure = f'exec get_user {user_id}'
    result = db.execute_procedure(procedure)[0]
    if result[0] == 'user not in db':
        return jsonify(error=response)
    else:
        user =  {'id': result[0], 'login': result[1], 'name': result[3],
                'surname': result[4], 'patronymic': result[5], 'phone_number': result[6]}
        return jsonify(user=user)




