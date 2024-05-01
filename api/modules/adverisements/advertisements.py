from flask import Blueprint, jsonify, request
from api.modules.auth.jwt_token import *
from api.DB.db import DB

advertisements = Blueprint('advertisements', __name__, url_prefix='/api/advertisements')
db = DB()
