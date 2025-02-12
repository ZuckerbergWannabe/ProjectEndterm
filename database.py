import sqlite3


class DatabaseManager:
    """Handles all database operations"""

    def __init__(self, db_name="inventory.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates tables for products and sales"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                quantity_sold INTEGER,
                total_price REAL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        ''')
        self.conn.commit()

    def execute_query(self, query, params=()):
        """Executes a query (INSERT, UPDATE, DELETE)"""
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query):
        """Fetches all results from a query"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
