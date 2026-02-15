"""
Solution 4: Guestbook - Add and List (Beginner, Simplest)
"""

from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'guestbook.db'

# Create table if not exists
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, message TEXT)')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        conn = sqlite3.connect(DATABASE)
        conn.execute('INSERT INTO entries (name, message) VALUES (?, ?)', (name, message))
        conn.commit()
        conn.close()
        return redirect('/')
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute('SELECT * FROM entries')
    entries = cur.fetchall()
    conn.close()
    return render_template('guestbook.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
