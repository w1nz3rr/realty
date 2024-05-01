from flask import Blueprint
from api.DB.db import DB

advertisements = Blueprint('advertisements', __name__, url_prefix='/api/advertisements')
db = DB()
