from database import Database

class Product:
    def __init__(self, db):
        self.db = db

    def add_product(self, name, description, price, quantity):
        query = "INSERT INTO product (name, description, price, quantity) VALUES (%s, %s, %s, %s)"
        values = (name, description, price, quantity)
        self.db.execute_query(query, values)

    def remove_product(self, product_id):
        query = "DELETE FROM product WHERE id = %s"
        self.db.execute_query(query, (product_id,))

    def update_product(self, product_id, field, value):
        query = f"UPDATE product SET {field} = %s WHERE id = %s"
        self.db.execute_query(query, (value, product_id))

