"""
Solution 2: Feedback Collector with Advanced Filtering and Batch Delete (Advanced)
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'secret'
DATABASE = 'feedback.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def index():
    init_db()
    keywords = request.args.get('keywords', '').strip()
    conn = sqlite3.connect(DATABASE)
    if keywords:
        kw_list = keywords.split()
        query = 'SELECT * FROM feedback WHERE ' + ' OR '.join(['message LIKE ?' for _ in kw_list]) + ' ORDER BY id DESC'
        params = [f'%{kw}%' for kw in kw_list]
        cur = conn.execute(query, params)
    else:
        cur = conn.execute('SELECT * FROM feedback ORDER BY id DESC')
    feedbacks = cur.fetchall()
    conn.close()
    return render_template('feedback.html', feedbacks=feedbacks)

@app.route('/add', methods=['POST'])
def add_feedback():
    message = request.form['message']
    conn = sqlite3.connect(DATABASE)
    conn.execute('INSERT INTO feedback (message) VALUES (?)', (message,))
    conn.commit()
    conn.close()
    flash('Feedback added!')
    return redirect(url_for('index'))

@app.route('/batch_delete', methods=['POST'])
def batch_delete():
    ids = request.form.getlist('ids')
    if not ids:
        flash('No feedback selected!')
        return redirect(url_for('index'))
    conn = sqlite3.connect(DATABASE)
    for fid in ids:
        conn.execute('DELETE FROM feedback WHERE id=?', (fid,))
    conn.commit()
    conn.close()
    flash('Selected feedback deleted!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
