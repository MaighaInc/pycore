"""
Solution for Assignment 4: Employee Directory (Intermediate)
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

# 2. Insert at least 4 employees
employees = [
    (1, 'John Doe', 'IT'),
    (2, 'Jane Smith', 'HR'),
    (3, 'Alice Brown', 'Finance'),
    (4, 'Bob White', 'IT')
]
cursor.executemany("INSERT INTO employees (id, name, department) VALUES (?, ?, ?)", employees)
conn.commit()

# 3. Select and print all employees in the 'IT' department
cursor.execute("SELECT * FROM employees WHERE department = 'IT'")
results = cursor.fetchall()
print("Employees in IT department:")
for row in results:
    print(row)

# 4. Update the department of one employee
cursor.execute("UPDATE employees SET department = 'Finance' WHERE id = 4")
conn.commit()

# 5. Print all employee names in reverse order
cursor.execute("SELECT name FROM employees")
names = [row[0] for row in cursor.fetchall()]
print("Employee names in reverse order:")
for name in reversed(names):
    print(name)

conn.close()
