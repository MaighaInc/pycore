"""
Solution for Assignment 4: Employee Directory (Advanced)
"""

import sqlite3

# 1. Create database and table
conn = sqlite3.connect('company.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT
    )
""")

# 2. Insert at least 6 employees
employees = [
    (1, 'John Doe', 'Finance'),
    (2, 'Jane Smith', 'IT'),
    (3, 'Alice Brown', 'Finance'),
    (4, 'Bob White', 'HR'),
    (5, 'Sara Black', 'Finance'),
    (6, 'Tom Green', 'IT')
]
cursor.executemany("INSERT INTO employees (id, name, department) VALUES (?, ?, ?)", employees)
conn.commit()

# 3. Select and print all employees in the 'Finance' department, ordered by name
cursor.execute("SELECT * FROM employees WHERE department = 'Finance' ORDER BY name")
results = cursor.fetchall()
print("Employees in Finance department:")
for row in results:
    print(row)

# 4. Update the department of one employee
cursor.execute("UPDATE employees SET department = 'HR' WHERE id = 5")
conn.commit()

# 5. Delete one employee by id
cursor.execute("DELETE FROM employees WHERE id = 4")
conn.commit()

# 6. Print all unique department names in uppercase
cursor.execute("SELECT DISTINCT department FROM employees")
departments = [row[0].upper() for row in cursor.fetchall()]
print("Departments (uppercase):")
for dept in departments:
    print(dept)

conn.close()
