from flask import Flask, request
from api.auth.auth import auth
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.register_blueprint(auth)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'SECRET_KEY'

if __name__ == '__main__':
    app.run()
