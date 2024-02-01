import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Erreur MySQL: {err}")

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
