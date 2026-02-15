"""
Solution 4: Guestbook - Add, List, Edit, Delete (Intermediate)
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'guestbook.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, message TEXT)')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def index():
    init_db()
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute('SELECT * FROM entries')
    entries = cur.fetchall()
    conn.close()
    return render_template('guestbook.html', entries=entries, edit_entry=None)

@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    message = request.form['message']
    conn = sqlite3.connect(DATABASE)
    conn.execute('INSERT INTO entries (name, message) VALUES (?, ?)', (name, message))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    init_db()
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        conn = sqlite3.connect(DATABASE)
        conn.execute('UPDATE entries SET name=?, message=? WHERE id=?', (name, message, entry_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute('SELECT * FROM entries')
    entries = cur.fetchall()
    cur2 = conn.execute('SELECT * FROM entries WHERE id=?', (entry_id,))
    edit_entry = cur2.fetchone()
    conn.close()
    return render_template('guestbook.html', entries=entries, edit_entry=edit_entry)

@app.route('/delete/<int:entry_id>')
def delete_entry(entry_id):
    conn = sqlite3.connect(DATABASE)
    conn.execute('DELETE FROM entries WHERE id=?', (entry_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
