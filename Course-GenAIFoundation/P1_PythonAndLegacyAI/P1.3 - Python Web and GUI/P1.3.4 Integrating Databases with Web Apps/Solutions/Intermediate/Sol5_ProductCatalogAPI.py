"""
Solution 5: Product Catalog REST API - Add, List, Update, Delete (Intermediate)
"""

from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'products.db'

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

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    if not data or ('name' not in data and 'price' not in data):
        return jsonify({'error': 'Invalid input'}), 400
    conn = sqlite3.connect(DATABASE)
    if 'name' in data and 'price' in data:
        conn.execute('UPDATE products SET name=?, price=? WHERE id=?', (data['name'], data['price'], product_id))
    elif 'name' in data:
        conn.execute('UPDATE products SET name=? WHERE id=?', (data['name'], product_id))
    elif 'price' in data:
        conn.execute('UPDATE products SET price=? WHERE id=?', (data['price'], product_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product updated'})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute('DELETE FROM products WHERE id=?', (product_id,))
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'message': 'Product deleted'})

if __name__ == '__main__':
    app.run(debug=True)
