"""
Assignment 3: Library Book Tracker (Advanced)

Scenario:
You are building a robust library book tracker using SQLite and Python.

Objective:
- Create a database and table for books
- Insert multiple book records
- Select books by author and title pattern
- Update and delete book records
- Use Python to print the author with the most books

Tasks:
1. Create a SQLite database 'library.db' and a table 'books' (id INTEGER PRIMARY KEY, title TEXT, author TEXT).
2. Insert at least 7 books with different titles and authors.
3. Select and print all books by an author whose name contains 'a' (case-insensitive).
4. Update the title of one book (choose any).
5. Delete one book by id (choose any).
6. Use Python to print the author who has the most books in the table.

Hints:
- Use the sqlite3 module in Python
- Use SQL's LIKE operator for author pattern
- Use Python's collections.Counter to count books per author

Rubric:
- Table created: 15%
- Records inserted: 20%
- Select, update, delete: 35%
- Python author count: 30%
"""