"""
Solution for Assignment 1: Student Database Manager (Intermediate)
"""

import sqlite3

# 1. Create database and table
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER,
        name TEXT,
        grade INTEGER
    )
""")

# 2. Insert at least 4 students
students = [
    (101, 'Alice', 80),
    (102, 'Bob', 90),
    (103, 'Anil', 70),
    (104, 'Sara', 85)
]
cursor.executemany("INSERT INTO students (id, name, grade) VALUES (?, ?, ?)", students)
conn.commit()

# 3. Select and print all students with grade above 75
cursor.execute("SELECT * FROM students WHERE grade > 75")
results = cursor.fetchall()
print("Students with grade above 75:")
for row in results:
    print(row)

# 4. Update the grade of one student
cursor.execute("UPDATE students SET grade = 95 WHERE id = 102")
conn.commit()

# 5. Calculate and print the average grade using Python
cursor.execute("SELECT grade FROM students")
grades = [row[0] for row in cursor.fetchall()]
avg_grade = sum(grades) / len(grades) if grades else 0
print("Average grade:", avg_grade)

conn.close()
