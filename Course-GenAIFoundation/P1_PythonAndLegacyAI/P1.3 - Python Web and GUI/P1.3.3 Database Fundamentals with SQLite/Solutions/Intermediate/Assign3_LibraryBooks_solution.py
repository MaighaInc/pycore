"""
Solution for Assignment 3: Library Book Tracker (Intermediate)
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

# 2. Insert at least 4 books
books = [
    (1, '1984', 'George Orwell'),
    (2, 'The Hobbit', 'J.R.R. Tolkien'),
    (3, 'The Alchemist', 'Paulo Coelho'),
    (4, 'Animal Farm', 'George Orwell')
]
cursor.executemany("INSERT INTO books (id, title, author) VALUES (?, ?, ?)", books)
conn.commit()

# 3. Update the title of one book
cursor.execute("UPDATE books SET title = 'The Great Gatsby' WHERE id = 2")
conn.commit()

# 4. Select and print all books whose titles contain the word 'the' (case-insensitive)
cursor.execute("SELECT * FROM books WHERE LOWER(title) LIKE '%the%'")
results = cursor.fetchall()
print("Books with 'the' in the title:")
for row in results:
    print(row)

# 5. Print all unique authors sorted alphabetically
cursor.execute("SELECT DISTINCT author FROM books")
authors = sorted([row[0] for row in cursor.fetchall()])
print("Authors (sorted):")
for author in authors:
    print(author)

conn.close()
