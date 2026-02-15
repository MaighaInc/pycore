"""
Solution 1: Contact Book - Add, List, Edit, Delete (Intermediate)
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'contacts.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def index():
    init_db()
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute('SELECT * FROM contacts')
    contacts = cur.fetchall()
    conn.close()
    return render_template('contacts.html', contacts=contacts, edit_contact=None)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    email = request.form['email']
    conn = sqlite3.connect(DATABASE)
    conn.execute('INSERT INTO contacts (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    init_db()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = sqlite3.connect(DATABASE)
        conn.execute('UPDATE contacts SET name=?, email=? WHERE id=?', (name, email, contact_id))
        conn.commit()
        conn.close()
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
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
