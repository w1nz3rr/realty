from flask import Flask

app = Flask(__name__)

modules = {
    'users': {
        'auth': True,
        'users': True,
        'other': True,
        'requisites': True,
        'reviews': True
    },
    'agents':{
        'company': True,
        'specialist': True
    },
    'subject':{
        'objects': True,
        'advertisements': True

    }
}

if modules['users']['auth']:
    from api.modules.users.auth.auth import auth
    app.register_blueprint(auth)

if modules['users']['users']:
    from api.modules.users.users import users
    app.register_blueprint(users)

if modules['users']['other']:
    from api.modules.users.other.blacklist import blacklist
    app.register_blueprint(blacklist)
    from api.modules.users.other.complaints import complaints
    app.register_blueprint(complaints)
    from api.modules.users.other.me import me
    app.register_blueprint(me)
    from api.modules.users.other.favourites import favourites
    app.register_blueprint(favourites)

if modules['users']['requisites']:
    from api.modules.users.requisites.requisites import requisites
    app.register_blueprint(requisites)
    from api.modules.users.requisites.requisite import requisite
    app.register_blueprint(requisite)

if modules['agents']['company']:
    from api.modules.agents.company.companyes import companyes
    app.register_blueprint(companyes)
    from api.modules.agents.company.company import company
    app.register_blueprint(company)

if modules['agents']['specialist']:
    from api.modules.agents.specialist.specialists import specialists
    app.register_blueprint(specialists)
    from api.modules.agents.specialist.specialist import specialist
    app.register_blueprint(specialist)

if modules['subject']['objects']:
    from api.modules.subject.objects.objects import objects
    app.register_blueprint(objects)
    from api.modules.subject.objects.object import object
    app.register_blueprint(object)

if modules['subject']['advertisements']:
    from api.modules.subject.advertisements.advertisements import advertisements
    app.register_blueprint(advertisements)
    from api.modules.subject.advertisements.advertisement import advertisement
    app.register_blueprint(advertisement)

if modules['users']['reviews']:
    from api.modules.users.reviews.reviews import reviews
    app.register_blueprint(reviews)
