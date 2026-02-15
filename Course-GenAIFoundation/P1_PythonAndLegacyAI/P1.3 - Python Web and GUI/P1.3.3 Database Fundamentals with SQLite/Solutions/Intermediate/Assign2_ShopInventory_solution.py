"""
Solution for Assignment 2: Simple Shop Inventory (Intermediate)
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

# 2. Insert at least 4 products
products = [
    (1, 'Pen', 10.5),
    (2, 'Notebook', 25.0),
    (3, 'Eraser', 5.0),
    (4, 'Pencil', 8.0)
]
cursor.executemany("INSERT INTO products (id, name, price) VALUES (?, ?, ?)", products)
conn.commit()

# 3. Select and print all products whose names contain the letter 'e'
cursor.execute("SELECT * FROM products WHERE name LIKE '%e%'")
results = cursor.fetchall()
print("Products with 'e' in the name:")
for row in results:
    print(row)

# 4. Delete one product by id
cursor.execute("DELETE FROM products WHERE id = 3")
conn.commit()

# 5. Calculate and print the total value of all products
cursor.execute("SELECT price FROM products")
prices = [row[0] for row in cursor.fetchall()]
total_value = sum(prices)
print("Total inventory value:", total_value)

conn.close()
