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
        add_window = tk.Toplevel(self.root)
        add_window.title("Ajouter Produit")

        attributes = ["Nom", "Description", "Prix", "Quantité", "Catégorie"]
        entry_values = []
        for i, attribute in enumerate(attributes):
            tk.Label(add_window, text=attribute).grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(add_window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entry_values.append(entry)

        def add_product_to_db():
            values = [entry.get() for entry in entry_values]
            self.product.add_product(*values[:4])
            add_window.destroy()
            self.load_products()

        tk.Button(add_window, text="Ajouter", command=add_product_to_db).grid(row=len(attributes), columnspan=2, pady=10)


    def remove_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            product_id = self.tree.item(selected_item, 'values')[0]
            self.product.remove_product(product_id)
            self.load_products()

    def edit_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            product_id = self.tree.item(selected_item, 'values')[0]
            product_details = self.db.fetch_all(f"SELECT * FROM product WHERE id = {product_id}")

            if product_details:
                edit_window = tk.Toplevel(self.root)
                edit_window.title("Modifier Produit")

                attributes = ["Nom", "Description", "Prix", "Quantité", "Catégorie"]
                entry_values = []
                for i, attribute in enumerate(attributes):
                    tk.Label(edit_window, text=attribute).grid(row=i, column=0, padx=5, pady=5)
                    entry = tk.Entry(edit_window)
                    entry.grid(row=i, column=1, padx=5, pady=5)
                    entry.insert(tk.END, str(product_details[0][i + 1]))
                    entry_values.append(entry)

            def update_product():
                new_values = [entry.get() for entry in entry_values]
                attributes_to_update = ["name", "description", "price", "quantity", "id_category"]
                for attribute, value in zip(attributes_to_update, new_values):
                    self.product.update_product(product_id, attribute, value)

                edit_window.destroy()
                self.load_products()

            tk.Button(edit_window, text="Mettre à jour", command=update_product).grid(row=len(attributes), columnspan=2, pady=10)

        else:
            print("Erreur: Produit non trouvé.")



if __name__ == "__main__":
    db = Database(host="localhost", user="root", password="310104", database="store")
    product = Product(db)
    category = Category(db)

    root = tk.Tk()
    app = MainApp(root, db, product, category)
    root.mainloop()