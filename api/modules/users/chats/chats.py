from flask import Blueprint, jsonify, request
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

chats = Blueprint('chats', __name__, url_prefix='/api/users/chats')
db = DB()

@chats.get('/')
@jwt_required()
def get_chats():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec get_chats {self_id}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no chats')
    response = []
    for res in result:
        response.append({
            'chat_id': res[0],
            'advertisements_id': res[1],
            'last_message': res[2],
            'last_sender_id': res[3]
        })
    return jsonify(chats=response)

@chats.post('/')
@jwt_required()
def post_chats():
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json

    procedure = f'exec post_chats {self_id}, {body.get("advertisements_id", None)}, {body.get("message", None)}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no message')
    if result[0][0] == 'chat in db':
        return jsonify(error='chat in db')
    response = []
    for res in result:
        response.append({
            'message_id': res[0],
            'chat_id': res[1],
            'sender_id': res[2],
            'message': res[3]
        })
    return jsonify(messages=response)

