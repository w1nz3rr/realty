from flask import Blueprint, jsonify, request
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

requisites = Blueprint('requisites', __name__, url_prefix='/api/users/me/requisites')
db = DB()

@requisites.get('/')
@jwt_required()
def get_requisites():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec get_requisites {self_id}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no requisites')
    response = []
    for res in result:
        response.append({'requisite_id': res[0], 'BIC': res[2], 'recipient': res[3]})
    return jsonify(requisites=response)

@requisites.post('/')
@jwt_required()
def post_requisites():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json

    procedure = f'exec post_requisites {self_id}, {body["BIC"]}, {body["recipient"]}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no requisites')
    elif result[0][0] == 'requisites in db':
        return jsonify(error='requisites in db')
    response = []
    for res in result:
        response.append({'requisite_id': res[0], 'BIC': res[2], 'recipient': res[3]})
    return jsonify(requisites=response)
