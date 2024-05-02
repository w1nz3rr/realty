from flask import Blueprint, jsonify, request
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

advertisements = Blueprint('advertisements', __name__, url_prefix='/api/advertisements')
db = DB()

@advertisements.get('/')
@jwt_required()
def get_advertisements():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec get_advertisements {self_id}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no advertisements')
    response = []
    for res in result:
        response.append({
            'advertisements_id': res[0],
            'object_id': res[2],
            'title': res[3],
            'description': res[4]
        })
    return jsonify(advertisements=response)

@advertisements.post('/')
@jwt_required()
def post_advertisements():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json

    procedure = f'exec post_advertisements {self_id}, {body.get("object_id", None)}, {body.get("title", None)}, {body.get("description", None)}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no advertisements')
    elif result[0][0] == 'advertisements in db':
        return jsonify(error='advertisements in db')
    elif result[0][0] == 'bad object_id':
        return jsonify(error='bad object_id')
    response = []
    for res in result:
        response.append({
            'advertisements_id': res[0],
            'object_id': res[2],
            'title': res[3],
            'description': res[4]
        })
    return jsonify(advertisements=response)
