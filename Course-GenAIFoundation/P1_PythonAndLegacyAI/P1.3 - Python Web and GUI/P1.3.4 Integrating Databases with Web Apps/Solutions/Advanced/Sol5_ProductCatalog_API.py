from flask import Flask, jsonify, request
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB = 'products.db'

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL
        )''')

@app.route('/products', methods=['GET'])
def get_products():
    keyword = request.args.get('keyword', '').strip()
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    category = request.args.get('category', '').strip()
    query = 'SELECT id, name, price, category FROM products WHERE 1=1'
    params = []
    if keyword:
        for word in keyword.split():
            query += ' AND name LIKE ?'
            params.append(f'%{word}%')
    if min_price is not None:
        query += ' AND price >= ?'
        params.append(min_price)
    if max_price is not None:
        query += ' AND price <= ?'
        params.append(max_price)
    if category:
        query += ' AND category = ?'
        params.append(category)
    query += ' ORDER BY price ASC'
    with sqlite3.connect(DB) as conn:
        cur = conn.execute(query, params)
        products = [dict(id=row[0], name=row[1], price=row[2], category=row[3]) for row in cur.fetchall()]
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name', '').strip()
    price = data.get('price')
    category = data.get('category', '').strip()
    if not name or price is None or not category:
        return jsonify({'error': 'Name, price, and category required.'}), 400
    with sqlite3.connect(DB) as conn:
        conn.execute('INSERT INTO products (name, price, category) VALUES (?, ?, ?)', (name, price, category))
    return jsonify({'message': 'Product added!'}), 201

@app.route('/products/batch_delete', methods=['POST'])
def batch_delete():
    ids = request.json.get('ids', [])
    if not ids:
        return jsonify({'error': 'No products selected.'}), 400
    with sqlite3.connect(DB) as conn:
        conn.executemany('DELETE FROM products WHERE id=?', [(i,) for i in ids])
    return jsonify({'message': f'{len(ids)} product(s) deleted.'})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    with sqlite3.connect(DB) as conn:
        conn.execute('DELETE FROM products WHERE id=?', (product_id,))
    return jsonify({'message': 'Product deleted.'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
