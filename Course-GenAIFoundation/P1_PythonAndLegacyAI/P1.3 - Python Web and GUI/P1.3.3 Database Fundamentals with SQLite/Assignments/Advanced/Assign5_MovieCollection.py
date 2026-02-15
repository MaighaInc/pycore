"""
Assignment 5: Movie Collection (Advanced)

Scenario:
You are building a robust movie collection using SQLite and Python.

Objective:
- Create a database and table for movies
- Insert multiple movie records
- Select movies by title pattern
- Update and delete movie records
- Use Python to print the average release year of all movies

Tasks:
1. Create a SQLite database 'movies.db' and a table 'movies' (id INTEGER PRIMARY KEY, title TEXT, year INTEGER).
2. Insert at least 7 movies with different titles and years.
3. Select and print all movies whose titles contain the letter 'a' (case-insensitive).
4. Update the year of one movie (choose any).
5. Delete one movie by id (choose any).
6. Use Python to calculate and print the average release year of all movies in the table.

Hints:
- Use the sqlite3 module in Python
- Use SQL's LIKE operator for title pattern
- Use Python's sum() and len() for average

Rubric:
- Table created: 15%
- Records inserted: 20%
- Select, update, delete: 35%
- Python average year: 30%
"""