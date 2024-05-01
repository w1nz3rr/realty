from flask import Blueprint, jsonify, request
from api.modules.auth.jwt_token import *
from api.DB.db import DB

requisite = Blueprint('requisite', __name__, url_prefix='/api/users/me/requisites/<requisite_id>')
db = DB()

@requisite.get('/')
@jwt_required()
def get_requisites(requisite_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec get_requisite {self_id}, {requisite_id}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no requisites')
    response = {'requisite_id': result[0][0], 'BIC': result[0][2], 'recipient': result[0][3]}
    return jsonify(requisite=response)

@requisite.put('/')
@jwt_required()
def put_requisites(requisite_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json

    procedure = f'exec put_requisite {self_id}, {requisite_id}, {body["BIC"]}, {body["recipient"]}'
    result = db.execute_procedure(procedure)
    if result[0] == 'recipient not in db':
        return jsonify(error='recipient not in db')
    else:
        response = {'requisite_id': result[0][0], 'BIC': result[0][2], 'recipient': result[0][3]}
        return jsonify(requisite=response)

@requisite.delete('/')
@jwt_required()
def delete_requisites(requisite_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec delete_requisite {self_id}, {requisite_id}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no requisites')
    elif result[0] == 'recipient not in db':
        return jsonify(error='recipient not in db')
    else:
        return jsonify(requisite=result[0][0])