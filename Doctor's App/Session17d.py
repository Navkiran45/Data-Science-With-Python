
import mysql.connector as mydb
class Database:
    def __init__(self):
        self.connection = mydb.connect(user= "root", password="0811", host ="127.0.0.1", database= "training")
        print("[Database] connection created")

        self.cursor = self.connection.cursor()
        print("[Database] Cursor created")

    def write(self, sql):
        print("[Database] SQL Statement", sql)
        self.cursor.execute(sql)
        self.connection.commit()
        print("SQL Statement Executed Successfully..")

    def read(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result