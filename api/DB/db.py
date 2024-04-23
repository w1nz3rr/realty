import pyodbc


class DB:
    data_connect = r'Driver={SQL Server};Server=DB_Realty.mssql.somee.com;Database=DB_Realty;UID=nnnnnn1k_SQLLogin_1;PWD=9lmrvly3rc'
    connect = None
    cursor = None
    cache = None
    error = None

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connect = pyodbc.connect(self.data_connect)
        self.cursor = self.connect.cursor()

    def execute_query(self, query, *args, is_select=False):
        flag = True
        if not self.cursor_execute(query, args):
            flag = False
        if is_select:
            flag = self.select()
        self.cursor.commit()
        return flag

    def cursor_execute(self, query, args):
        try:
            if args:
                self.cursor.execute(query, args)
            else:
                self.cursor.execute(query)
            return True
        except pyodbc.Error as e:
            print(e)
            return False

    def select(self):
        try:
            self.cache = self.cursor.fetchall()
            return True
        except:
            return False

    def close_connection(self):
        self.cursor.close()
        self.connect.close()


