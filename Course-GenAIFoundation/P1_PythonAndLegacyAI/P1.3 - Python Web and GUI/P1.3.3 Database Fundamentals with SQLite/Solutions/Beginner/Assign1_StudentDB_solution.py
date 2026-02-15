"""
Solution for Assignment 1: Student Database Manager (Beginner)
"""

import sqlite3

# 1. Create database and table
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER,
        name TEXT
    )
""")

# 2. Insert at least 3 students
students = [
    (101, 'Alice'),
    (102, 'Bob'),
    (103, 'Anil')
]
cursor.executemany("INSERT INTO students (id, name) VALUES (?, ?)", students)
conn.commit()

# 3. Select and print all students whose names start with 'A'
cursor.execute("SELECT * FROM students WHERE name LIKE 'A%'")
results = cursor.fetchall()
print("Students whose names start with 'A':")
for row in results:
    print(row)

# 4. Count and print the number of students whose names start with 'A'
print("Total students with names starting with 'A':", len(results))

conn.close()
