"""
Solution 2: Feedback Collector - Add and List (Beginner, Simplest)
"""

from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'feedback.db'

# Create table if not exists
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    if request.method == 'POST':
        message = request.form['message']
        conn = sqlite3.connect(DATABASE)
        conn.execute('INSERT INTO feedback (message) VALUES (?)', (message,))
        conn.commit()
        conn.close()
        return redirect('/')
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute('SELECT * FROM feedback')
    feedbacks = cur.fetchall()
    conn.close()
    return render_template('feedback.html', feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
