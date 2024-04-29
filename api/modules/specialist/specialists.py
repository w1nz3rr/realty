from flask import Blueprint, jsonify, request, abort
from api.modules.auth.jwt_token import *
from api.DB.db import DB

specialists = Blueprint('specialists', __name__, url_prefix='/api/specialists/<type>')
db = DB()

@specialists.get('/')
def get_specialists(type):
    procedure = f'exec get_specialists {type}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no specialists')
    elif result[0][0] == 'error':
        return abort(404)
    else:
        results = []
        for res in result:
            results.append({'specialists_id': res[0], 'name': res[1], 'surname': res[2], 'patronymic': res[3],
                            'phone_number': res[4], 'license_number': res[5]})

        return jsonify({f'{type}_specialists': results})

@specialists.post('/')
def post_specialists(type):
    body = request.json
    procedure = f'exec post_specialists {type}, {body["name"]}, {body["surname"]}, {body["patronymic"]}, {body["phone_number"]}, {body["license_number"]}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no specialists')
    elif result[0][0] == 'error':
        return abort(404)
    else:
        results = []
        for res in result:
            results.append({'specialists_id': res[0], 'name': res[1], 'surname': res[2], 'patronymic': res[3],
                            'phone_number': res[4], 'license_number': res[5]})

        return jsonify({f'{type}_specialists': results})

