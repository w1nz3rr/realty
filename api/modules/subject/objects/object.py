from flask import Blueprint, jsonify, request
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

object = Blueprint('object', __name__, url_prefix='/api/objects/<object_id>')
db = DB()

@object.get('/')
@jwt_required()
def get_object(object_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec get_object {self_id}, {object_id}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no objects')
    response = {'objects_id': result[0][0], 'type_object': result[0][1], 'purpose':result[0][2],
                         'address': {
                            'street': result[0][3],
                             'district': result[0][4],
                             'city': result[0][5],
                             'area': result[0][6],
                             'house_number': result[0][7],
                             'apartment_number': result[0][8],
                             'floor': result[0][9]
                         }, 'passport_id': result[0][10], 'square': result[0][11], 'number_of_rooms': result[0][12]}
    return jsonify(objects=response)

@object.put('/')
@jwt_required()
def put_object(object_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json
    address = request.json.get("address", None)


    procedure = f'exec put_object {self_id}, {object_id}, {body.get("type_object", None)}, {body.get("purpose", None)},' \
                f' {address.get("street", None)}, {address.get("district", None)}, {address.get("city", None)},' \
                f' {address.get("area", None)}, {address.get("house_number", None)}, {address.get("apartment_number", None)},' \
                f'{address.get("floor", 0)}, {body.get("passport_id", 1)}, {body.get("square", 0)}, {body.get("number_of_rooms", 0)}'
    result = db.execute_procedure(procedure)
    if result[0][0] == 'object not in db':
        return jsonify(error='object not in db')
    response = {'objects_id': result[0][0], 'type_object': result[0][1], 'purpose': result[0][2],
                'address': {
                    'street': result[0][3],
                    'district': result[0][4],
                    'city': result[0][5],
                    'area': result[0][6],
                    'house_number': result[0][7],
                    'apartment_number': result[0][8],
                    'floor': result[0][9]
                }, 'passport_id': result[0][10], 'square': result[0][11], 'number_of_rooms': result[0][12]}
    return jsonify(objects=response)