"""
Solution 5: Product Catalog REST API - Add and List (Beginner, Simplest)
"""

from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'products.db'

# Create table if not exists
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)')
    conn.commit()
    conn.close()

@app.route('/products', methods=['GET'])
def get_products():
    init_db()
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute('SELECT * FROM products')
    products = [{'id': row[0], 'name': row[1], 'price': row[2]} for row in cur.fetchall()]
    conn.close()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    init_db()
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    conn = sqlite3.connect(DATABASE)
    conn.execute('INSERT INTO products (name, price) VALUES (?, ?)', (data['name'], data['price']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product added'}), 201

if __name__ == '__main__':
    app.run(debug=True)
