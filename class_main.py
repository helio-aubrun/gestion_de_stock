import tkinter as tk
from tkinter import ttk
from database import Database
from product import Product
from category import Category

class MainApp:
    def __init__(self, root, db, product, category):
        self.root = root
        self.db = db
        self.product = product
        self.category = category

        self.root.title("Gestion de Stock")

        self.create_gui()

        self.load_products()

    def create_gui(self):
        columns = ("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=20)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        btn_add = tk.Button(btn_frame, text="Ajouter Produit", command=self.add_product)
        btn_add.grid(row=0, column=0, padx=5)

        btn_remove = tk.Button(btn_frame, text="Supprimer Produit", command=self.remove_product)
        btn_remove.grid(row=0, column=1, padx=5)

        btn_edit = tk.Button(btn_frame, text="Modifier Produit", command=self.edit_product)
        btn_edit.grid(row=0, column=2, padx=5)

    def load_products(self):
        products = self.db.fetch_all("SELECT * FROM product")

        for row in self.tree.get_children():
            self.tree.delete(row)

        for product in products:
            self.tree.insert("", "end", values=product)

    def add_product(self):
        # Ajouter un produit dans la base de données
        # Vous devriez créer une nouvelle fenêtre pour saisir les détails du produit
        # et gérer l'insertion dans la base de données.

        # Exemple d'utilisation :
        self.product.add_product("Nouveau Produit", "Description", 10, 100, 1)

        # Après l'insertion, appelez load_products() pour mettre à jour le tableau.
        self.load_products()

    def remove_product(self):
        # Supprimer un produit de la base de données
        selected_item = self.tree.selection()
        if selected_item:
            product_id = self.tree.item(selected_item, 'values')[0]
            self.product.remove_product(product_id)
            self.load_products()

    def edit_product(self):
        # Modifier un produit dans la base de données
        selected_item = self.tree.selection()
        if selected_item:
            product_id = self.tree.item(selected_item, 'values')[0]
            # Vous devriez créer une nouvelle fenêtre pour modifier les détails du produit
            # et gérer la mise à jour dans la base de données.

            # Exemple d'utilisation :
            self.product.update_product(product_id, "price", 15)

            # Après la mise à jour, appelez load_products() pour mettre à jour le tableau.
            self.load_products()

if __name__ == "__main__":
    # Initialise la base de données et les classes associées
    db = Database(host="localhost", user="root", password="310104", database="store")
    product = Product(db)
    category = Category(db)

    # Crée et lance l'application principale
    root = tk.Tk()
    app = MainApp(root, db, product, category)
    root.mainloop()