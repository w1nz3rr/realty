from flask import Blueprint, jsonify, request, abort
from api.modules.auth.jwt_token import *
from api.DB.db import DB

company = Blueprint('company', __name__, url_prefix='/api/company/<type>')
db = DB()

@company.get('/')
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



@company.post('/')
def post_companyes(type):
    name = request.json.get('company_name', None)
    phone = request.json.get('phone_number', None)

    procedure = f'exec post_companyes {type}, {name}, {phone}'
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

@company.get('/<company_id>')
def get_company(type, company_id):
    procedure = f'exec get_company {type}, {company_id}'
    result = db.execute_procedure(procedure)[0]
    if not result:
        return jsonify(error='no company')
    elif result[0] == 'error':
        return abort(404)
    else:
        response = {'company_id': result[0], 'company_name': result[1], 'phone_number': result[2]}
        return jsonify({f'{type}_company': response})
@company.put('/<company_id>')
def put_company(type, company_id):
    name = request.json.get('company_name', None)
    phone = request.json.get('phone_number', None)

    procedure = f'exec put_company {type},{company_id}, {name}, {phone}'
    result = db.execute_procedure(procedure)[0]
    if not result:
        return jsonify(error='no company')
    elif result[0] == 'error':
        return abort(404)
    else:
        response = {'company_id': result[0], 'company_name': result[1], 'phone_number': result[2]}
        return jsonify({f'{type}_company': response})