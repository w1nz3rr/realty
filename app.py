from flask import Flask
from flask_jwt_extended import JWTManager
from api.modules.auth.auth import auth
from api.modules.users.users import users
from api.modules.users.blacklist import blacklist
from api.modules.company.companyes import companyes
from api.modules.company.company import company
from api.modules.users.complaints import complaints
from api.modules.specialist.specialists import specialists
from api.modules.specialist.specialist import specialist
from api.modules.users.me import me
from api.modules.users.requisites.requisites import requisites
from api.modules.users.requisites.requisite import requisite
from api.modules.users.favourites import favourites


app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'SECRET_KEY'

app.register_blueprint(auth)
app.register_blueprint(users)
app.register_blueprint(blacklist)
app.register_blueprint(companyes)
app.register_blueprint(complaints)
app.register_blueprint(company)
app.register_blueprint(specialists)
app.register_blueprint(specialist)
app.register_blueprint(me)
app.register_blueprint(requisites)
app.register_blueprint(requisite)
app.register_blueprint(favourites)

if __name__ == '__main__':
    app.run()
