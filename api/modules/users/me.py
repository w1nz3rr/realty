from flask import Blueprint, jsonify, request
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

me = Blueprint('me', __name__, url_prefix='/api/users/me')
db = DB()

@me.get('/')
@jwt_required()
def get_me():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec get_me {self_id}'
    result = db.execute_procedure(procedure)[0]
    response = {'id': result[0], 'login': result[1], 'name': result[3],
                'surname': result[4], 'patronymic': result[5], 'phone_number': result[6]}
    return jsonify(user=response)

@me.put('/<change>')
@jwt_required()
def put_me(change):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json
    if change == 'password':
        procedure = f'exec change_password {self_id}, {body["password"]}'
    elif change == 'phone':
        procedure = f'exec change_phone {self_id}, {body["phone_number"]}'
    else:
        procedure = f'exec change_me {self_id}, {body["name"]}, {body["surname"]}, {body["patronymic"]}'
    result = db.execute_procedure(procedure)[0]
    response = {'id': result[0], 'login': result[1], 'name': result[3],
                'surname': result[4], 'patronymic': result[5], 'phone_number': result[6]}
    return jsonify(user=response)