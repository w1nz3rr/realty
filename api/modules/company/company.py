from flask import Blueprint, jsonify, request, abort
from api.apiclass.CompanyAPI import CompanyAPI
from api.modules.auth.jwt_token import *

company = Blueprint('company', __name__, url_prefix='/api/company')

@company.get('/<type>')
def get_companyes(type):
    companyAPI = CompanyAPI()
    response = companyAPI.get_companyes(type)
    if response == 'error':
        return abort(404)
    elif response == 'no company':
        return jsonify(error='no company')
    else:
        comp = type+'company'
        return jsonify(comp=response)

@company.post('/<type>')
def post_companyes(type):
    companyAPI = CompanyAPI()
    name = request.json.get('company_name', None)
    phone = request.json.get('phone_number', None)
    response = companyAPI.post_companyes(type, name, phone)
    if response == 'error':
        return abort(404)
    elif response == 'no company':
        return jsonify(error='no company')
    else:
        comp = type + 'company'
        return jsonify(comp=response)