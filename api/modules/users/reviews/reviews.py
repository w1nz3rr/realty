from flask import Blueprint, jsonify, request
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

reviews = Blueprint('reviews', __name__, url_prefix='/api/users/reviews')
db = DB()

@reviews.get('/')
@jwt_required()
def get_reviews():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec get_reviews {self_id}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no reviews')
    response = []
    for res in result:
        response.append({
            'review_id': res[0],
            'advertisements_id': res[1],
            'estimation': res[3],
            'description': res[4]
        })
    return jsonify(reviews=response)

@reviews.post('/')
@jwt_required()
def post_reviews():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json

    procedure = f'exec post_reviews {self_id}, {body.get("object_id", None)}, {body.get("estimation")}, {body.get("description")}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no reviews')
    elif result[0][0] == 'review in db':
        return jsonify(error='review in db')
    response = []
    for res in result:
        response.append({
            'review_id': res[0],
            'advertisements_id': res[1],
            'estimation': res[3],
            'description': res[4]
        })
    return jsonify(reviews=response)

@reviews.delete('/<review_id>')
@jwt_required()
def delete_review(review_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec delete_review {self_id}, {review_id}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no reviews')
    elif result[0][0] == 'review not in db':
        return jsonify(error='review not in db')
    return jsonify(status=result[0][0])
