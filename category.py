from database import Database

class Category:
    def __init__(self, db):
        self.db = db

    def add_category(self, name):
        query = "INSERT INTO category (name) VALUES (%s)"
        self.db.execute_query(query, (name,))

    def remove_category(self, category_id):
        query = "DELETE FROM category WHERE id = %s"
        self.db.execute_query(query, (category_id,))
