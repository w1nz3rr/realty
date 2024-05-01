from flask import Blueprint, jsonify, request
from api.modules.auth.jwt_token import *
from api.DB.db import DB

objects = Blueprint('objects', __name__, url_prefix='/api/objects')
db = DB()

@objects.get('/')
@jwt_required()
def get_objects():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec get_objects {self_id}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no objects')
    response = []
    for res in result:
        response.append({'objects_id': res[0], 'type_object': res[1], 'purpose':res[2],
                         'address': {
                            'street': res[3],
                             'district': res[4],
                             'city': res[5],
                             'area': res[6],
                             'house_number': res[7],
                             'apartment_number': res[8],
                             'floor': res[9]
                         }, 'passport_id': res[10], 'square': res[11], 'number_of_rooms': res[12]})
    return jsonify(objects=response)

@objects.post('/')
@jwt_required()
def post_objects():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json
    address = request.json.get("address", None)


    procedure = f'exec post_objects {self_id}, {body.get("type_object", None)}, {body.get("purpose", None)},' \
                f' {address.get("street", None)}, {address.get("district", None)}, {address.get("city", None)},' \
                f' {address.get("area", None)}, {address.get("house_number", None)}, {address.get("apartment_number", None)},' \
                f'{address.get("floor", None)}, {body.get("passport_id", 1)}, {body.get("square", 0)}, {body.get("number_of_rooms", 0)}'
    result = db.execute_procedure(procedure)
    if result[0][0] == 'object in db':
        return jsonify(error='object in db')
    response = []
    for res in result:
        response.append({'objects_id': res[0], 'type_object': res[1], 'purpose': res[2],
                         'address': {
                             'street': res[3],
                             'district': res[4],
                             'city': res[5],
                             'area': res[6],
                             'house_number': res[7],
                             'apartment_number': res[8],
                             'floor': res[9]
                         }, 'passport_id': res[10], 'square': res[11], 'number_of_rooms': res[12]})
    return jsonify(objects=response)