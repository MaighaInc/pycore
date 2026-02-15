"""
Assignment 5: Movie Collection (Intermediate)

Scenario:
You are building a movie collection using SQLite and Python.

Objective:
- Create a database and table for movies
- Insert multiple movie records
- Select movies released after a certain year
- Delete a movie by id
- Use Python to print the shortest movie title (fewest characters)

Tasks:
1. Create a SQLite database called 'movies.db' and a table 'movies' (id INTEGER, title TEXT, year INTEGER).
2. Insert at least 4 movies with different years and titles.
3. Select and print all movies released after 2015.
4. Delete one movie by id (choose any).
5. Use Python to print the movie title (from the table) with the fewest characters (shortest title).

Hints:
- Use the sqlite3 module in Python
- Use SQL's WHERE clause for year filtering
- Use Python's min() with key=len for shortest title

Rubric:
- Table created: 20%
- Records inserted: 20%
- Select and delete: 30%
- Python shortest title print: 30%
"""