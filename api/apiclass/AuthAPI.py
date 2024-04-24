from api.DB.db import DB

class AuthAPI(DB):
    def registration(self, user):
        procedure = f'exec registration {user.login}, {user.password}, {user.name}, {user.surname}, {user.patronymic}, {user.phone_number}'
        result = self.execute_procedure(procedure)[0]
        if result[0] == 'user in db':
            return 'user in db'
        else:
            user.id = result[0]
        return user.__dict__

    def authorization(self, login, password):
        procedure = f'exec login {login}, {password}'
        result = self.execute_procedure(procedure)[0]
        if result[0] == 'user not in db':
            return 'user not in db'
        else:
            return {'id': result[0], 'login': result[1], 'name': result[3],
                    'surname': result[4], 'patronymic': result[5], 'phone_number': result[6]}

