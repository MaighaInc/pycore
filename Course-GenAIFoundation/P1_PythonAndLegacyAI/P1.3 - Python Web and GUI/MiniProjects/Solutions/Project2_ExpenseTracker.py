"""
Mini Project 2: Expense Tracker with SQLite (Solution)
"""

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/expenses', methods=['GET'])
def get_expenses():
    conn = get_db_connection()
    expenses = conn.execute('SELECT * FROM expenses').fetchall()
    conn.close()
    return jsonify([dict(row) for row in expenses])

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)', (data['amount'], data['category'], data['description']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Expense added'}), 201

@app.route('/expenses/<int:id>', methods=['PUT'])
def update_expense(id):
    data = request.get_json()
    conn = get_db_connection()
    conn.execute('UPDATE expenses SET amount = ?, category = ?, description = ? WHERE id = ?', (data['amount'], data['category'], data['description'], id))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Expense updated'})

@app.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Expense deleted'})

if __name__ == '__main__':
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, amount REAL, category TEXT, description TEXT)')
    conn.close()
    app.run(debug=True)
