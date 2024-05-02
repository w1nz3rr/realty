from flask import Blueprint, jsonify, request
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

advertisement = Blueprint('advertisement', __name__, url_prefix='/api/advertisements/<advertisement_id>')
db = DB()

@advertisement.get('/')
@jwt_required()
def get_advertisement(advertisement_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec get_advertisement {self_id}, {advertisement_id}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no advertisements')
    response = {
            'advertisements_id': result[0][0],
            'object_id': result[0][2],
            'title': result[0][3],
            'description': result[0][4]
        }
    return jsonify(advertisement=response)

@advertisement.put('/')
@jwt_required()
def put_advertisement(advertisement_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json

    procedure = f'exec put_advertisement {self_id}, {advertisement_id}, {body.get("title", None)}, {body.get("description", None)}'
    result = db.execute_procedure(procedure)

    if result[0][0] == 'advertisements not in db':
        return jsonify(error='advertisements not in db')
    response = {
        'advertisements_id': result[0][0],
        'object_id': result[0][2],
        'title': result[0][3],
        'description': result[0][4]
    }
    return jsonify(advertisement=response)

@advertisement.delete('/')
@jwt_required()
def delete_advertisement(advertisement_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec delete_advertisement {self_id}, {advertisement_id}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no advertisements')
    elif result[0][0] == 'advertisements not in db':
        return jsonify(error='advertisements not in db')
    return jsonify(status=result[0][0])