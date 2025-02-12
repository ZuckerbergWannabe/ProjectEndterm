import tkinter as tk
from tkinter import ttk, messagebox
from database import DatabaseManager
from product import Product
from sales import Sale

class InventoryApp:
    """Main GUI Application"""

    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.db = DatabaseManager()

        self.create_widgets()

    def create_widgets(self):
        """Creates GUI Components"""
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Product Management Fields
        tk.Label(frame, text="Product Name").grid(row=0, column=0)
        self.product_name = tk.Entry(frame)
        self.product_name.grid(row=0, column=1)

        tk.Label(frame, text="Category").grid(row=0, column=2)
        self.category = tk.Entry(frame)
        self.category.grid(row=0, column=3)

        tk.Label(frame, text="Quantity").grid(row=1, column=0)
        self.quantity = tk.Entry(frame)
        self.quantity.grid(row=1, column=1)

        tk.Label(frame, text="Price").grid(row=1, column=2)
        self.price = tk.Entry(frame)
        self.price.grid(row=1, column=3)

        tk.Button(frame, text="Add Product", command=self.add_product).grid(row=2, column=0, columnspan=2)

        # Table for displaying inventory
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Category", "Quantity", "Price"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.pack()

        tk.Button(self.root, text="Refresh Inventory", command=self.load_products).pack()

    def add_product(self):
        """Adds a product"""
        name = self.product_name.get()
        category = self.category.get()
        quantity = int(self.quantity.get())
        price = float(self.price.get())

        self.db.execute_query("INSERT INTO products (name, category, quantity, price) VALUES (?, ?, ?, ?)",
                              (name, category, quantity, price))
        messagebox.showinfo("Success", "Product Added!")
        self.load_products()

    def load_products(self):
        """Loads products into the table"""
        self.tree.delete(*self.tree.get_children())
        products = self.db.fetch_all("SELECT * FROM products")
        for prod in products:
            self.tree.insert("", "end", values=prod)
