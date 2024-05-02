from flask import Blueprint, jsonify, request, abort
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

specialist = Blueprint('specialist', __name__, url_prefix='/api/specialists/<type>/<specialist_id>')
db = DB()

@specialist.get('/')
def get_specialist(type, specialist_id):
    procedure = f'exec get_specialist {type}, {specialist_id}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no specialist')
    elif result[0][0] == 'error':
        return abort(404)
    else:
        response = {'specialists_id': result[0][0], 'name': result[0][1], 'surname': result[0][2],
                    'patronymic': result[0][3], 'phone_number': result[0][4], 'license_number': result[0][5]}
        return jsonify({f'{type}_specialist': response})

@specialist.put('/')
def put_specialist(type, specialist_id):
    body = request.json
    procedure = f'exec put_specialist {type}, {specialist_id}, {body["name"]}, {body["surname"]}, {body["patronymic"]}, {body["phone_number"]}, {body["license_number"]}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no specialist')
    elif result[0][0] == 'error':
        return abort(404)
    else:
        response = {'specialists_id': result[0][0], 'name': result[0][1], 'surname': result[0][2],
                    'patronymic': result[0][3], 'phone_number': result[0][4], 'license_number': result[0][5]}
        return jsonify({f'{type}_specialist': response})



@specialist.delete('/')
def delete_specialist(type, specialist_id):
    procedure = f'exec delete_specialist {type}, {specialist_id}'
    result = db.execute_procedure(procedure)
    if result[0][0] == 'error':
        return abort(404)
    else:
        return jsonify(status=result[0][0])