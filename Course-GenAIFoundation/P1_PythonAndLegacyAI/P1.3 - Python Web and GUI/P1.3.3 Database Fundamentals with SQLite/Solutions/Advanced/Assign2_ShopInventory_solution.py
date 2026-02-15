"""
Solution for Assignment 2: Simple Shop Inventory (Advanced)
"""

import sqlite3

# 1. Create database and table
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
""")

# 2. Insert at least 6 products
products = [
    (1, 'Pen', 10.5),
    (2, 'Notebook', 25.0),
    (3, 'Eraser', 5.0),
    (4, 'Pencil', 8.0),
    (5, 'Marker', 15.0),
    (6, 'Folder', 30.0)
]
cursor.executemany("INSERT INTO products (id, name, price) VALUES (?, ?, ?)", products)
conn.commit()

# 3. Update the price of one product
cursor.execute("UPDATE products SET price = 35.0 WHERE id = 6")
conn.commit()

# 4. Delete one product by id
cursor.execute("DELETE FROM products WHERE id = 3")
conn.commit()

# 5. Select and print all products with price between 15 and 50, ordered by price
cursor.execute("SELECT * FROM products WHERE price BETWEEN 15 AND 50 ORDER BY price")
results = cursor.fetchall()
print("Products with price between 15 and 50:")
for row in results:
    print(row)

# 6. Print all product names sorted by length (shortest to longest)
cursor.execute("SELECT name FROM products")
names = [row[0] for row in cursor.fetchall()]
for name in sorted(names, key=len):
    print(name)

conn.close()
