"""
Solution for Assignment 5: Movie Collection (Intermediate)
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

# 2. Insert at least 4 movies
movies = [
    (1, 'Inception', 2010),
    (2, 'Arrival', 2016),
    (3, 'Avatar', 2009),
    (4, 'Up', 2017)
]
cursor.executemany("INSERT INTO movies (id, title, year) VALUES (?, ?, ?)", movies)
conn.commit()

# 3. Select and print all movies released after 2015
cursor.execute("SELECT * FROM movies WHERE year > 2015")
results = cursor.fetchall()
print("Movies released after 2015:")
for row in results:
    print(row)

# 4. Delete one movie by id
cursor.execute("DELETE FROM movies WHERE id = 3")
conn.commit()

# 5. Print the shortest movie title using Python
cursor.execute("SELECT title FROM movies")
titles = [row[0] for row in cursor.fetchall()]
if titles:
    shortest = min(titles, key=len)
    print("Shortest movie title:", shortest)
else:
    print("No movies found.")

conn.close()
