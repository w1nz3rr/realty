from flask import Flask, Blueprint, request, jsonify
from api.auth.AuthAPI import AuthAPI
from api.auth.jwt_token import *

auth = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth.post('/registration')
def register_user():
    Auth = AuthAPI()
    login = request.json['login']
    password = request.json['password']
    confirm_password = request.json['confirm_password']
    nickname = request.json['nickname']
    error = user_valid.validate_register(login, password, confirm_password, nickname)
    if error:
        return jsonify(error=error)

    Auth.registration(login, password, nickname)

    if Auth.error == "Данный логин занят":
        return jsonify(error="Данный логин занят")

    user = Auth.user.__dict__
    token = create_token({'id': user['id']})
    del user['password']
    return jsonify(user=user, token=token)


@auth.post('/login')
def login_user():
    Auth = AuthAPI()
    login = request.json['login']
    password = request.json['password']
    Auth.login(login, password)
    print(request.json)
    print(Auth.error)
    if Auth.error == 'Нет такого пользователя':
        #abort(401)
        return jsonify(error="Неверный логин или пароль")

    user = Auth.user.__dict__
    token = create_token({'id': user['id']})
    del user['password']
    return jsonify(user=user, token=token)
