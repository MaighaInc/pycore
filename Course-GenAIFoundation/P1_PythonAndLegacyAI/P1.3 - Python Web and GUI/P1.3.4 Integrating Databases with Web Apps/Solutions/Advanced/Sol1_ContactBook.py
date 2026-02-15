"""
Solution 1: Contact Book with Advanced Search and Batch Edit (Advanced)
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'secret'
DATABASE = 'contacts.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        group_name TEXT
    )''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def index():
    init_db()
    name = request.args.get('name', '')
    email = request.args.get('email', '')
    phone = request.args.get('phone', '')
    conn = sqlite3.connect(DATABASE)
    query = 'SELECT * FROM contacts WHERE 1=1'
    params = []
    if name:
        query += ' AND name LIKE ?'
        params.append(f'%{name}%')
    if email:
        query += ' AND email LIKE ?'
        params.append(f'%{email}%')
    if phone:
        query += ' AND phone LIKE ?'
        params.append(f'%{phone}%')
    cur = conn.execute(query, params)
    contacts = cur.fetchall()
    conn.close()
    return render_template('contacts.html', contacts=contacts, edit_contact=None)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    conn = sqlite3.connect(DATABASE)
    # Prevent duplicate email
    cur = conn.execute('SELECT * FROM contacts WHERE email=?', (email,))
    if cur.fetchone():
        conn.close()
        flash('Duplicate email!')
        return redirect(url_for('index'))
    conn.execute('INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
    conn.commit()
    conn.close()
    flash('Contact added!')
    return redirect(url_for('index'))

@app.route('/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    init_db()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        conn = sqlite3.connect(DATABASE)
        conn.execute('UPDATE contacts SET name=?, email=?, phone=? WHERE id=?', (name, email, phone, contact_id))
        conn.commit()
        conn.close()
        flash('Contact updated!')
        return redirect(url_for('index'))
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute('SELECT * FROM contacts')
    contacts = cur.fetchall()
    cur2 = conn.execute('SELECT * FROM contacts WHERE id=?', (contact_id,))
    edit_contact = cur2.fetchone()
    conn.close()
    return render_template('contacts.html', contacts=contacts, edit_contact=edit_contact)

@app.route('/delete/<int:contact_id>')
def delete_contact(contact_id):
    conn = sqlite3.connect(DATABASE)
    conn.execute('DELETE FROM contacts WHERE id=?', (contact_id,))
    conn.commit()
    conn.close()
    flash('Contact deleted!')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
