from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = 'supersecretkey'
DB = 'tasks.db'

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            due_date TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )''')

@app.route('/', methods=['GET'])
def index():
    keyword = request.args.get('keyword', '').strip()
    due_from = request.args.get('due_from', '')
    due_to = request.args.get('due_to', '')
    filter_status = request.args.get('filter', 'all')
    query = 'SELECT id, description, due_date, completed FROM tasks WHERE 1=1'
    params = []
    if keyword:
        for word in keyword.split():
            query += ' AND description LIKE ?'
            params.append(f'%{word}%')
    if due_from:
        query += ' AND due_date >= ?'
        params.append(due_from)
    if due_to:
        query += ' AND due_date <= ?'
        params.append(due_to)
    if filter_status == 'completed':
        query += ' AND completed = 1'
    elif filter_status == 'incomplete':
        query += ' AND completed = 0'
    query += ' ORDER BY due_date ASC'
    with sqlite3.connect(DB) as conn:
        cur = conn.execute(query, params)
        tasks = [list(row) for row in cur.fetchall()]
    # Mark overdue
    for t in tasks:
        t.append((not t[3]) and (t[2] < date.today().isoformat()))
    return render_template('tasks.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    desc = request.form['description'].strip()
    due = request.form['due_date']
    if not desc or not due:
        flash('Description and due date required.')
        return redirect(url_for('index'))
    with sqlite3.connect(DB) as conn:
        conn.execute('INSERT INTO tasks (description, due_date) VALUES (?, ?)', (desc, due))
    flash('Task added!')
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    with sqlite3.connect(DB) as conn:
        conn.execute('UPDATE tasks SET completed=1 WHERE id=?', (task_id,))
    flash('Task marked as completed.')
    return redirect(url_for('index'))

@app.route('/batch_complete', methods=['POST'])
def batch_complete():
    ids = request.form.getlist('ids')
    if not ids:
        flash('No tasks selected.')
        return redirect(url_for('index'))
    with sqlite3.connect(DB) as conn:
        conn.executemany('UPDATE tasks SET completed=1 WHERE id=?', [(i,) for i in ids])
    flash(f'{len(ids)} task(s) marked as completed.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
