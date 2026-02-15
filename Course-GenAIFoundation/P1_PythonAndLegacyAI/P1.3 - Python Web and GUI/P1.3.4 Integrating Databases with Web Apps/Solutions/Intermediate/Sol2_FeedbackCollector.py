"""
Solution 2: Feedback Collector - Add, List, Filter (Intermediate)
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
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
    filter_kw = request.args.get('filter', '')
    conn = sqlite3.connect(DATABASE)
    if filter_kw:
        cur = conn.execute('SELECT * FROM feedback WHERE message LIKE ? ORDER BY id DESC', (f'%{filter_kw}%',))
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
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
