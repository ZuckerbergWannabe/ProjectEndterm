class Product:
    """Represents a product in the inventory"""

    def __init__(self, product_id, name, category, quantity, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def update_quantity(self, new_quantity):
        """Updates the quantity of the product"""
        self.quantity = new_quantity

    def update_price(self, new_price):
        """Updates the price of the product"""
        self.price = new_price
