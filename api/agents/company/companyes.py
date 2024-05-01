from flask import Blueprint, jsonify, request, abort
from api.modules.auth.jwt_token import *
from api.DB.db import DB

companyes = Blueprint('companyes', __name__, url_prefix='/api/companyes/<type>')
db = DB()

@companyes.get('/')
def get_companyes(type):
    procedure = f'exec get_companyes {type}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no company')
    elif result[0][0] == 'error':
        return abort(404)
    else:
        results = []
        for res in result:
            results.append({'company_id': res[0], 'company_name': res[1], 'phone_number': res[2]})
        return jsonify({f'{type}_company': results})

@companyes.post('/')
def post_companyes(type):
    body = request.json

    procedure = f'exec post_companyes {type}, {body["name"]}, {body["phone_number"]}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no company')
    elif result[0][0] == 'error':
        return abort(404)
    else:
        results = []
        for res in result:
            results.append({'company_id': res[0], 'company_name': res[1], 'phone_number': res[2]})
        return jsonify({f'{type}_company': results})
