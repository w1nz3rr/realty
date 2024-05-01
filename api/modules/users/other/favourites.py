from flask import Blueprint, jsonify, request
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

favourites = Blueprint('favourites', __name__, url_prefix='/api/users/me/favourites')
db = DB()

@favourites.get('/')
@jwt_required()
def get_favourites():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec get_favourites {self_id}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no favourites')
    response = []
    for res in result:
        response.append({'favourite_id': res[0], 'advertisements_id': res[1]})
    return jsonify(favourite=response)

@favourites.post('/')
@jwt_required()
def post_favourites():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json

    procedure = f'exec post_favourites {self_id}, {body["advertisements_id"]}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no favourites')
    elif result[0][0] == 'favourites in db':
        return jsonify(error='favourites in db')
    response = []
    for res in result:
        response.append({'favourite_id': res[0], 'advertisements_id': res[1]})
    return jsonify(favourite=response)

@favourites.delete('/<favourite_id>')
@jwt_required()
def delete_favourite(favourite_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json

    procedure = f'exec delete_favourite {self_id}, {favourite_id}'
    result = db.execute_procedure(procedure)
    if result[0][0] == 'no favourites':
        return jsonify(error='no favourites')
    return jsonify(favourite=result[0][0])