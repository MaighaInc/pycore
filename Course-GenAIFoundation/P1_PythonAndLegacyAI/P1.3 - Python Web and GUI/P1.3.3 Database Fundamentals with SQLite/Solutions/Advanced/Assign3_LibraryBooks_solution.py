"""
Solution for Assignment 3: Library Book Tracker (Advanced)
"""

import sqlite3
from collections import Counter

# 1. Create database and table
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT
    )
""")

# 2. Insert at least 7 books
books = [
    (1, '1984', 'George Orwell'),
    (2, 'The Hobbit', 'J.R.R. Tolkien'),
    (3, 'The Alchemist', 'Paulo Coelho'),
    (4, 'Animal Farm', 'George Orwell'),
    (5, 'Brida', 'Paulo Coelho'),
    (6, 'The Pilgrimage', 'Paulo Coelho'),
    (7, 'The Silmarillion', 'J.R.R. Tolkien')
]
cursor.executemany("INSERT INTO books (id, title, author) VALUES (?, ?, ?)", books)
conn.commit()

# 3. Select and print all books by an author whose name contains 'a' (case-insensitive)
cursor.execute("SELECT * FROM books WHERE LOWER(author) LIKE '%a%'")
results = cursor.fetchall()
print("Books by authors with 'a' in their name:")
for row in results:
    print(row)

# 4. Update the title of one book
cursor.execute("UPDATE books SET title = 'The Great Gatsby' WHERE id = 2")
conn.commit()

# 5. Delete one book by id
cursor.execute("DELETE FROM books WHERE id = 5")
conn.commit()

# 6. Print the author with the most books using Python
cursor.execute("SELECT author FROM books")
authors = [row[0] for row in cursor.fetchall()]
if authors:
    most_common = Counter(authors).most_common(1)[0]
    print("Author with most books:", most_common[0], "with", most_common[1], "books")
else:
    print("No authors found.")

conn.close()
