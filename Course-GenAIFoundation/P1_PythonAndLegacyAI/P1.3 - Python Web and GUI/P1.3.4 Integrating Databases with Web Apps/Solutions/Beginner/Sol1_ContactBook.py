"""
Solution 1: Contact Book - Add and List (Beginner, Simplest)
"""

from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'contacts.db'

# Create table if not exists
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = sqlite3.connect(DATABASE)
        conn.execute('INSERT INTO contacts (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        conn.close()
        return redirect('/')
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute('SELECT * FROM contacts')
    contacts = cur.fetchall()
    conn.close()
    return render_template('contacts.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)
