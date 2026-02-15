"""
Solution for Assignment 3: Library Book Tracker (Beginner)
"""

import sqlite3

# 1. Create database and table
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER,
        title TEXT,
        author TEXT
    )
""")

# 2. Insert at least 3 books
books = [
    (1, '1984', 'George Orwell'),
    (2, 'The Hobbit', 'J.R.R. Tolkien'),
    (3, 'Animal Farm', 'George Orwell')
]
cursor.executemany("INSERT INTO books (id, title, author) VALUES (?, ?, ?)", books)
conn.commit()

# 3. Select and print all books by a specific author
author = 'George Orwell'
cursor.execute("SELECT * FROM books WHERE author = ?", (author,))
results = cursor.fetchall()
print(f"Books by {author}:")
for row in results:
    print(row)

# 4. Print all book titles in uppercase using Python
cursor.execute("SELECT title FROM books")
titles = [row[0] for row in cursor.fetchall()]
print("All book titles in uppercase:")
for title in titles:
    print(title.upper())

conn.close()
