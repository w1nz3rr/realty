from flask import Blueprint, jsonify, request
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

messages = Blueprint('messages', __name__, url_prefix='/api/users/chats/<chat_id>/messages')
db = DB()

@messages.get('/')
@jwt_required()
def get_messages(chat_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)

    procedure = f'exec get_messages {self_id}, {chat_id}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no messages')
    response = []
    for res in result:
        response.append({
            'message_id': res[0],
            'chat_id': res[1],
            'sender_id': res[2],
            'message': res[3]
        })
    return jsonify(messages=response)

@messages.post('/')
@jwt_required()
def post_messages(chat_id):
    token = request.headers['Authorization']
    self_id = decode_jwt(token)
    body = request.json

    procedure = f'exec post_messages {self_id}, {chat_id}, {body.get("message", None)}'
    result = db.execute_procedure(procedure)

    if not result:
        return jsonify(error='no message')
    if result[0][0] == 'chat not in db':
        return jsonify(error='chat not in db')
    response = []
    for res in result:
        response.append({
            'message_id': res[0],
            'chat_id': res[1],
            'sender_id': res[2],
            'message': res[3]
        })
    return jsonify(messages=response)