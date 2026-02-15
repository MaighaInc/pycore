"""
Solution 3: Task Tracker - Add and List (Beginner, Simplest)
"""

from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'tasks.db'

# Create table if not exists
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT)')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    if request.method == 'POST':
        description = request.form['description']
        conn = sqlite3.connect(DATABASE)
        conn.execute('INSERT INTO tasks (description) VALUES (?)', (description,))
        conn.commit()
        conn.close()
        return redirect('/')
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    conn.close()
    return render_template('tasks.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
