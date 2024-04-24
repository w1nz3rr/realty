from flask import Flask
from api.modules.auth.auth import auth
from api.modules.users.users import users
from api.modules.users.blacklist import blacklist
from api.modules.company.company import company
from api.modules.users.complaints import complaints
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(users)
app.register_blueprint(blacklist)
app.register_blueprint(company)
app.register_blueprint(complaints)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'SECRET_KEY'

if __name__ == '__main__':
    app.run()
