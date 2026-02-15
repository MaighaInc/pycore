from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'
DB = 'guestbook.db'

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            date TEXT NOT NULL
        )''')

@app.route('/', methods=['GET'])
def index():
    keyword = request.args.get('keyword', '').strip()
    date_from = request.args.get('date_from', '')
    date_to = request.args.get('date_to', '')
    query = 'SELECT id, name, message, date FROM guests WHERE 1=1'
    params = []
    if keyword:
        for word in keyword.split():
            query += ' AND (name LIKE ? OR message LIKE ?)'
            params.extend([f'%{word}%', f'%{word}%'])
    if date_from:
        query += ' AND date >= ?'
        params.append(date_from)
    if date_to:
        query += ' AND date <= ?'
        params.append(date_to)
    query += ' ORDER BY date DESC'
    with sqlite3.connect(DB) as conn:
        cur = conn.execute(query, params)
        guests = cur.fetchall()
    return render_template('guestbook.html', guests=guests)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name'].strip()
    message = request.form['message'].strip()
    if not name or not message:
        flash('Name and message required.')
        return redirect(url_for('index'))
    today = datetime.now().date().isoformat()
    with sqlite3.connect(DB) as conn:
        conn.execute('INSERT INTO guests (name, message, date) VALUES (?, ?, ?)', (name, message, today))
    flash('Entry added!')
    return redirect(url_for('index'))

@app.route('/delete/<int:guest_id>')
def delete(guest_id):
    with sqlite3.connect(DB) as conn:
        conn.execute('DELETE FROM guests WHERE id=?', (guest_id,))
    flash('Entry deleted.')
    return redirect(url_for('index'))

@app.route('/batch_delete', methods=['POST'])
def batch_delete():
    ids = request.form.getlist('ids')
    if not ids:
        flash('No entries selected.')
        return redirect(url_for('index'))
    with sqlite3.connect(DB) as conn:
        conn.executemany('DELETE FROM guests WHERE id=?', [(i,) for i in ids])
    flash(f'{len(ids)} entr(y/ies) deleted.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
