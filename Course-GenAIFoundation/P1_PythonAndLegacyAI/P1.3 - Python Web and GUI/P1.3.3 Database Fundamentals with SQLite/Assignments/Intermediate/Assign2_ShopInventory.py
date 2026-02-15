"""
Assignment 2: Simple Shop Inventory (Intermediate)

Scenario:
You are managing a shop's inventory using SQLite and Python.

Objective:
- Create a database and table for products
- Insert multiple product records
- Select products with a name pattern
- Delete a product by id
- Use Python to calculate and print the total inventory value (sum of all prices)

Tasks:
1. Create a SQLite database called 'shop.db' and a table 'products' (id INTEGER, name TEXT, price REAL).
2. Insert at least 4 products with different names and prices.
3. Select and print all products whose names contain the letter 'e'.
4. Delete one product by id (choose any).
5. Use Python to calculate and print the total value of all products in inventory.

Hints:
- Use the sqlite3 module in Python
- Use SQL's LIKE operator for name pattern
- Use Python's sum() to total prices

Rubric:
- Table created: 20%
- Records inserted: 20%
- Select and delete: 30%
- Python total value calculation: 30%
"""