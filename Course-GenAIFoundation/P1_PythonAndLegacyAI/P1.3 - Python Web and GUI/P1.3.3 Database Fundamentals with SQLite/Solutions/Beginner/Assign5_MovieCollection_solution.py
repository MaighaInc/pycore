"""
Solution for Assignment 5: Movie Collection (Beginner)
"""

import sqlite3

# 1. Create database and table
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER,
        title TEXT,
        year INTEGER
    )
""")

# 2. Insert at least 3 movies
movies = [
    (1, 'Inception', 2010),
    (2, 'Arrival', 2016),
    (3, 'Avatar', 2009)
]
cursor.executemany("INSERT INTO movies (id, title, year) VALUES (?, ?, ?)", movies)
conn.commit()

# 3. Select and print all movies released after 2010
cursor.execute("SELECT * FROM movies WHERE year > 2010")
results = cursor.fetchall()
print("Movies released after 2010:")
for row in results:
    print(row)

# 4. Print all movie titles sorted alphabetically using Python
cursor.execute("SELECT title FROM movies")
titles = [row[0] for row in cursor.fetchall()]
print("All movie titles sorted alphabetically:")
for title in sorted(titles):
    print(title)

conn.close()
