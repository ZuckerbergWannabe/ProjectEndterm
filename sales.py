from product import Product


class Sale:
    """Handles sale transactions"""

    def __init__(self, product, quantity_sold):
        self.product = product
        self.quantity_sold = quantity_sold
        self.total_price = self.product.price * self.quantity_sold

    def process_sale(self, db):
        """Records the sale in the database and updates inventory"""
        db.execute_query("INSERT INTO sales (product_id, quantity_sold, total_price) VALUES (?, ?, ?)",
                         (self.product.product_id, self.quantity_sold, self.total_price))
        new_quantity = self.product.quantity - self.quantity_sold
        db.execute_query("UPDATE products SET quantity = ? WHERE id = ?",
                         (new_quantity, self.product.product_id))
