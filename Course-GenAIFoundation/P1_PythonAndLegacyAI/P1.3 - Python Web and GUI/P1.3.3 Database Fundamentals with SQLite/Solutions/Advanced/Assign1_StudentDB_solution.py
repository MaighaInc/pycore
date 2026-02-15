"""
Solution for Assignment 1: Student Database Manager (Advanced)
"""

import sqlite3

# 1. Create database and table
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER
    )
""")

# 2. Insert at least 6 students
students = [
    (1, 'Sam', 85),
    (2, 'Sara', 92),
    (3, 'Steve', 78),
    (4, 'Alice', 88),
    (5, 'Bob', 65),
    (6, 'Sonia', 90)
]
cursor.executemany("INSERT INTO students (id, name, grade) VALUES (?, ?, ?)", students)
conn.commit()

# 3. Select and print all students with grade above 70 and name starting with 'S', ordered by grade
cursor.execute("SELECT * FROM students WHERE grade > 70 AND name LIKE 'S%' ORDER BY grade")
results = cursor.fetchall()
print("Students with grade > 70 and name starting with 'S':")
for row in results:
    print(row)

# 4. Update the grade of one student
cursor.execute("UPDATE students SET grade = 95 WHERE id = 2")
conn.commit()

# 5. Delete one student by id
cursor.execute("DELETE FROM students WHERE id = 5")
conn.commit()

# 6. Print the highest and lowest grades using Python
cursor.execute("SELECT grade FROM students")
grades = [row[0] for row in cursor.fetchall()]
if grades:
    print("Highest grade:", max(grades))
    print("Lowest grade:", min(grades))
else:
    print("No grades found.")

conn.close()
