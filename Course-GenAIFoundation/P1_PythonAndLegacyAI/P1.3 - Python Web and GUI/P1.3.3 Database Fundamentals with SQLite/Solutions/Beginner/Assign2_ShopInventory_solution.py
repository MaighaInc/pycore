"""
Solution for Assignment 2: Simple Shop Inventory (Beginner)
"""

import sqlite3

# 1. Create database and table
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER,
        name TEXT,
        price REAL
    )
""")

# 2. Insert at least 3 products
products = [
    (1, 'Pen', 10.5),
    (2, 'Notebook', 25.0),
    (3, 'Eraser', 5.0)
]
cursor.executemany("INSERT INTO products (id, name, price) VALUES (?, ?, ?)", products)
conn.commit()

# 3. Select and print all products with price greater than 10
cursor.execute("SELECT * FROM products WHERE price > 10")
results = cursor.fetchall()
print("Products with price > 10:")
for row in results:
    print(row)

# 4. Find and print the most expensive product using Python
cursor.execute("SELECT name, price FROM products")
all_products = cursor.fetchall()
if all_products:
    most_expensive = max(all_products, key=lambda x: x[1])
    print("Most expensive product:", most_expensive[0], "with price", most_expensive[1])
else:
    print("No products found.")

conn.close()
