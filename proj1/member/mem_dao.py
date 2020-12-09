import cx_Oracle

class Dao:
    def __init__(self, id, pwd, address, enc):
        self.id = id
        self.pwd = pwd
        self.address = address
        self.enc = enc

    def __str__(self):
        return cx_Oracle.connect(self.id, self.pwd, self.address, self.enc)

        #conn = cx_Oracle.connect('hr', 'hr', 'localhost:1521/XE', encoding = 'utf-8')

    def disconnect(self, conn):
        conn.close()

    def insert(self, mem):
        pass

    def select(self, id):
        pass

    def selectAll(self):
        pass

    def update(self, mem):
        pass

    def delete(self, id):
        pass