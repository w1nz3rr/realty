from flask import Blueprint, jsonify, request, abort
from api.modules.auth.jwt_token import *
from api.DB.db import DB

company = Blueprint('company', __name__, url_prefix='/api/company')
db = DB()

@company.get('/<type>')
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
        comp = type + 'company'
        return jsonify({f'{type}_company': results})



@company.post('/<type>')
def post_companyes(type):
    name = request.json.get('company_name', None)
    phone = request.json.get('phone_number', None)

    procedure = f'exec post_companyes {table}, {name}, {phone}'
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