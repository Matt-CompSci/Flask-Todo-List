import sqlite3


class Database:
    def __init__(self, db_file):
        self.database = sqlite3.connect(db_file)

    def query(self, query_string):
        cur = self.database.cursor()
        cur.execute(query_string)
        return cur.fetchall()

    def __del__(self):
        self.database.close()

