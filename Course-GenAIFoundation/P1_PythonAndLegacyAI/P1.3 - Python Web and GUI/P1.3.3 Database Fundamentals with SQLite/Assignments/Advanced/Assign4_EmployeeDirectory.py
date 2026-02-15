"""
Assignment 4: Employee Directory (Advanced)

Scenario:
You are creating a robust employee directory using SQLite and Python.

Objective:
- Create a database and table for employees
- Insert multiple employee records
- Select employees by department
- Update and delete employee records
- Use Python to print all department names in uppercase

Tasks:
1. Create a SQLite database 'company.db' and a table 'employees' (id INTEGER PRIMARY KEY, name TEXT, department TEXT).
2. Insert at least 6 employees in different departments.
3. Select and print all employees in the 'Finance' department, ordered by name.
4. Update the department of one employee (choose any).
5. Delete one employee by id (choose any).
6. Use Python to print all unique department names (from the table) in uppercase letters.

Hints:
- Use the sqlite3 module in Python
- Use SQL's WHERE clause for department filtering
- Use Python's set() and str.upper() for uppercase

Rubric:
- Table created: 15%
- Records inserted: 20%
- Select, update, delete: 35%
- Python uppercase departments: 30%
"""