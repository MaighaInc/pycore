"""
Solution 3: Task Tracker - Add, List, Due Date, Completion (Intermediate)
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'tasks.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        due_date TEXT,
        completed INTEGER DEFAULT 0
    )''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def index():
    init_db()
    filter_status = request.args.get('filter', 'all')
    conn = sqlite3.connect(DATABASE)
    if filter_status == 'completed':
        cur = conn.execute('SELECT * FROM tasks WHERE completed=1')
    elif filter_status == 'incomplete':
        cur = conn.execute('SELECT * FROM tasks WHERE completed=0')
    else:
        cur = conn.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    conn.close()
    return render_template('tasks.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    description = request.form['description']
    due_date = request.form['due_date']
    conn = sqlite3.connect(DATABASE)
    conn.execute('INSERT INTO tasks (description, due_date, completed) VALUES (?, ?, 0)', (description, due_date))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    conn = sqlite3.connect(DATABASE)
    conn.execute('UPDATE tasks SET completed=1 WHERE id=?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
