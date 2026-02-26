from flask import Flask, g
import sqlite3

DATABASE = 'example.db'
app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.route('/')
def index():
    db = get_db()
    db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    db.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
    db.commit()
    users = db.execute('SELECT * FROM users').fetchall()
    return str(users)

if __name__ == '__main__':
    app.run(debug=True)