from flask_jwt_extended import create_access_token, decode_token, jwt_required
import datetime


def create_token(data):
    token = create_access_token(identity=data)
    return token

def decode_jwt(token):
    id = decode_token(token[7:])['sub']['id']
    return id
