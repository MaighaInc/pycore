"""
Assignment 2: Simple Shop Inventory (Advanced)

Scenario:
You are managing a shop's inventory using SQLite and Python.

Objective:
- Create a database and table for products
- Insert multiple product records
- Update and delete product records
- Select products within a price range
- Use Python to print all product names sorted by length (shortest to longest)

Tasks:
1. Create a SQLite database 'shop.db' and a table 'products' (id INTEGER PRIMARY KEY, name TEXT, price REAL).
2. Insert at least 6 products with different names and prices.
3. Update the price of one product (choose any).
4. Delete one product by id (choose any).
5. Select and print all products with price between 15 and 50, ordered by price.
6. Use Python to print all product names (from the table) sorted by length (shortest to longest).

Hints:
- Use the sqlite3 module in Python
- Use SQL's BETWEEN for price range
- Use Python's sorted() with key=len for name sorting

Rubric:
- Table created: 15%
- Records inserted: 20%
- Update, delete, select: 35%
- Python name sorting: 30%
"""