from flask import Blueprint, jsonify, request, abort
from api.DB.db import DB

company = Blueprint('company', __name__, url_prefix='/api/companyes/<type>/<company_id>')
db = DB()


@company.get('/')
def get_company(type, company_id):
    procedure = f'exec get_company {type}, {company_id}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no company')
    elif result[0][0] == 'error':
        return abort(404)
    else:
        response = {'company_id': result[0][0], 'company_name': result[0][1], 'phone_number': result[0][2]}
        return jsonify({f'{type}_company': response})

@company.put('/')
def put_company(type, company_id):
    body = request.json
    procedure = f'exec put_company {type}, {company_id}, {body["name"]}, {body["phone_number"]}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no company')
    elif result[0][0] == 'error':
        return abort(404)
    else:
        response = {'company_id': result[0][0], 'company_name': result[0][1], 'phone_number': result[0][2]}
        return jsonify({f'{type}_company': response})

@company.delete('/')
def delete_company(type, company_id):
    procedure = f'exec delete_company {type}, {company_id}'
    result = db.execute_procedure(procedure)
    if not result:
        return jsonify(error='no company')
    elif result[0][0] == 'error':
        return abort(404)
    else:
        return jsonify(status=result[0][0])

