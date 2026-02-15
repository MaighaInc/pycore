"""
Solution for Assignment 4: Employee Directory (Beginner)
"""

import sqlite3

# 1. Create database and table
conn = sqlite3.connect('company.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER,
        name TEXT,
        department TEXT
    )
""")

# 2. Insert at least 3 employees
employees = [
    (1, 'John Doe', 'HR'),
    (2, 'Jane Smith', 'IT'),
    (3, 'Alice Brown', 'Finance')
]
cursor.executemany("INSERT INTO employees (id, name, department) VALUES (?, ?, ?)", employees)
conn.commit()

# 3. Select and print all employees in the 'HR' department
cursor.execute("SELECT * FROM employees WHERE department = 'HR'")
results = cursor.fetchall()
print("Employees in HR department:")
for row in results:
    print(row)

# 4. Print the total number of employees using Python
cursor.execute("SELECT * FROM employees")
all_employees = cursor.fetchall()
print("Total number of employees:", len(all_employees))

conn.close()
