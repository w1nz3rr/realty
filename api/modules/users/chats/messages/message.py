from flask import Blueprint, jsonify, request
from api.modules.users.auth.jwt_token import *
from api.DB.db import DB

message = Blueprint('message', __name__, url_prefix='/api/users/chats/<chat_id>/messages/<message_id>')
db = DB()

@message.get('/')
@jwt_required()
def get_message(chat_id, message_id):
    pass

@message.put('/')
@jwt_required()
def put_message(chat_id, message_id):
    pass
