from flask import Blueprint, jsonify, request
from api.DB.db import DB
from api.modules.auth.jwt_token import *

complaints = Blueprint('complaints ', __name__, url_prefix='/api/users/<int:user_id>/complaints')
db = DB()

@jwt_required()
@complaints.get('/')
def get_complaints(user_id):
    pass

@jwt_required()
@complaints.post('/')
def post_complaints(user_id):
    pass

@jwt_required()
@complaints.put('/')
def put_complaints(user_id):
    pass

@jwt_required()
@complaints.delete('/')
def delete_complaints(user_id):
    pass