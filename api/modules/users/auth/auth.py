from flask import Blueprint, request, jsonify
from api.DB.db import DB
from api.modules.users.auth.jwt_token import create_token

auth = Blueprint('auth', __name__, url_prefix='/api/auth')
db = DB()

@auth.post('/registration')
def registration():
    user = request.json
    procedure = f'exec registration {user["login"]}, {user["password"]}, {user["name"]}, {user["surname"]}, {user["patronymic"]}, {user["phone_number"]}'
    result = db.execute_procedure(procedure)[0]
    if result[0] == 'user in db':
        return jsonify(error='Пользователь уже зарегистрирован')
    else:
        user['id'] = result[0]
    del user['password']
    token = create_token({'id': user['id']})
    return jsonify(user=user, token=token)

@auth.post('/authorization')
def authorization():
    login, password = request.json.get('login'), request.json.get('password')
    procedure = f'exec login {login}, {password}'
    result = db.execute_procedure(procedure)[0]
    if result[0] == 'user not in db':
        return jsonify(error='Неверный логин или пароль')

    user = {'id': result[0], 'login': result[1], 'name': result[3],
                'surname': result[4], 'patronymic': result[5], 'phone_number': result[6]}
    token = create_token({'id': user['id']})
    return jsonify(user=user, token=token)

