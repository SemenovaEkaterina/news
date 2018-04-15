import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('news.sqlite')
        self.cursor = self.conn.cursor()

    def get_records(self):
        self.cursor.execute("SELECT u.login, r.text FROM record as r INNER JOIN user as u ON (u.id=r.user);")
        return self.cursor.fetchall()

    def add_record(self, login, password, text):
        self.cursor.execute("SELECT * FROM user WHERE login='%s' and password='%s'" % (login, password))
        user = self.cursor.fetchone()
        self.cursor.execute("INSERT INTO record (text, user) VALUES ('%s','%s')" % (text, user[0]))
        self.conn.commit()

