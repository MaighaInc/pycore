"""
Assignment 3: Library Book Tracker (Intermediate)

Scenario:
You are building a library book tracker using SQLite and Python.

Objective:
- Create a database and table for books
- Insert multiple book records
- Update the title of one book
- Select books with a partial title match
- Use Python to print all authors in sorted order

Tasks:
1. Create a SQLite database called 'library.db' and a table 'books' (id INTEGER, title TEXT, author TEXT).
2. Insert at least 4 books with different titles and authors.
3. Update the title of one book (choose any).
4. Select and print all books whose titles contain the word 'the' (case-insensitive).
5. Use Python to print all unique authors from the table, sorted alphabetically.

Hints:
- Use the sqlite3 module in Python
- Use SQL's LIKE operator for partial title match
- Use Python's set() and sorted() for unique, sorted authors

Rubric:
- Table created: 20%
- Records inserted: 20%
- Update and select: 30%
- Python author sort/print: 30%
"""