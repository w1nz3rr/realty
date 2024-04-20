from api.DB.db import DB
from datetime import datetime

class AuthAPI(DB):


    def take_user(self, login):
        query = 'select * from users where login = ?'
        self.execute_query(query, login, is_select=True)

    def registration(self, login, password, nickname):
        self.take_user(login)
        if self.cache:
            self.error = 'Данный логин занят'
            return False
        query = 'insert into users (login, password, create_at, update_at, nickname) values (?, ?, ?, ?, ?)'
        date = datetime.now()
        self.execute_query(query, login, password, date, date, nickname, is_select=False)
        self.take_user(login)
        self.set_user()

    def login(self, login, password):
        query = 'select * from users where login = ? and password = ?'
        self.execute_query(query, login, password, is_select=True)
        self.set_user()


