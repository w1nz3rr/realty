from flask import Blueprint, jsonify, request, abort
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

specialists = Blueprint('specialists', __name__, url_prefix='/api/companyes/<type>/<company_id>/specialists/')
db = DB()

@specialists.get('/')
def get_specialists(type, company_id):
    procedure = f'exec get_specialists {type}, {company_id}'
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
def post_specialists(type, company_id):
    body = request.json
    procedure = f'exec post_specialists {type}, {company_id}, {body["name"]}, {body["surname"]}, {body["patronymic"]}, {body["phone_number"]}, {body["license_number"]}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no specialists')
    elif result[0][0] == 'error':
        return abort(404)
    elif result[0][0] == 'specialist in company':
        return jsonify(error='specialist in company')
    else:
        results = []
        for res in result:
            results.append({'specialists_id': res[0], 'name': res[1], 'surname': res[2], 'patronymic': res[3],
                            'phone_number': res[4], 'license_number': res[5]})

        return jsonify({f'{type}_specialists': results})

@specialists.delete('/<specialist_id>')
def delete_specailists(type, company_id, specialist_id):
    procedure = f'exec delete_specialists {type}, {company_id}, {specialist_id}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no specialist')
    elif result[0][0] == 'error':
        return abort(404)
    else:
        return jsonify(status=result[0][0])