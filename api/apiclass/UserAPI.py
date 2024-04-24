from api.DB.db import DB

class UserAPI(DB):

    def get_user(self, user_id):
        procedure = f'exec get_user {user_id}'
        result = self.execute_procedure(procedure)[0]
        if result[0] == 'user not in db':
            return 'user not in db'
        else:
            return {'id': result[0], 'login': result[1], 'name': result[3],
             'surname': result[4], 'patronymic': result[5], 'phone_number': result[6]}

    def post_blacklist(self, self_id, user_id):
        procedure = f'exec post_blacklist {self_id}, {user_id}'
        result = self.execute_procedure(procedure)[0]
        if result[0] == 'user in blacklist':
            return 'user in blacklist'
        else:
            return True

    def delete_blacklist(self, self_id, user_id):
        procedure = f'exec delete_blacklist {self_id}, {user_id}'
        result = self.execute_procedure(procedure)[0]
        if result[0] == 'user not in blacklist':
            return 'user not in blacklist'
        else:
            return True

