from api.settings import app
from datetime import timedelta
from flask_jwt_extended import JWTManager


jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'SECRET_KEY'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)


if __name__ == '__main__':
    app.run()
