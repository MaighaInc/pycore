"""
Solution for Assignment 5: Movie Collection (Advanced)
"""

import sqlite3

# 1. Create database and table
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT,
        year INTEGER
    )
""")

# 2. Insert at least 7 movies
movies = [
    (1, 'Inception', 2010),
    (2, 'Arrival', 2016),
    (3, 'Avatar', 2009),
    (4, 'Up', 2017),
    (5, 'Gravity', 2013),
    (6, 'Interstellar', 2014),
    (7, 'Amelie', 2001)
]
cursor.executemany("INSERT INTO movies (id, title, year) VALUES (?, ?, ?)", movies)
conn.commit()

# 3. Select and print all movies whose titles contain the letter 'a' (case-insensitive)
cursor.execute("SELECT * FROM movies WHERE LOWER(title) LIKE '%a%'")
results = cursor.fetchall()
print("Movies with 'a' in the title:")
for row in results:
    print(row)

# 4. Update the year of one movie
cursor.execute("UPDATE movies SET year = 2020 WHERE id = 2")
conn.commit()

# 5. Delete one movie by id
cursor.execute("DELETE FROM movies WHERE id = 3")
conn.commit()

# 6. Print the average release year using Python
cursor.execute("SELECT year FROM movies")
years = [row[0] for row in cursor.fetchall()]
avg_year = sum(years) / len(years) if years else 0
print("Average release year:", avg_year)

conn.close()
