from flask import Blueprint, request, jsonify
from api.apiclass.AuthAPI import AuthAPI
from api.DB.dbclass.humansclass import User
from api.modules.auth.jwt_token import create_token

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth.post('/registration')
def registration():
    authAPI = AuthAPI()
    user = User()
    body = request.json
    user.login, user.password, user.name, user.surname, user.patronymic, user.phone_number = body.values()
    response = authAPI.registration(user)
    if response == 'user in db':
        return jsonify(error='Пользователь уже зарегистрирован')
    del response['password']
    token = create_token({'id': response['id']})
    return jsonify(user=response, token=token)

@auth.post('/authorization')
def authorization():
    authAPI = AuthAPI()
    body = request.json
    login, password = body.get('login'), body.get('password')
    response = authAPI.authorization(login, password)
    if response == 'user not in db':
        return jsonify(error='Неверный логин или пароль')
    token = create_token({'id': response['id']})
    return jsonify(user=response, token=token)