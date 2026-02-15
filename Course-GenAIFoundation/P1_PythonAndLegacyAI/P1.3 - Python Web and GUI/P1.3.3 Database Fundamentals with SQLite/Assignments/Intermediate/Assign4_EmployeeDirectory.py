"""
Assignment 4: Employee Directory (Intermediate)

Scenario:
You are creating an employee directory using SQLite and Python.

Objective:
- Create a database and table for employees
- Insert multiple employee records
- Select employees by department
- Update the department of one employee
- Use Python to print all employee names in reverse order

Tasks:
1. Create a SQLite database called 'company.db' and a table 'employees' (id INTEGER, name TEXT, department TEXT).
2. Insert at least 4 employees in different departments.
3. Select and print all employees in the 'IT' department.
4. Update the department of one employee (choose any).
5. Use Python to print all employee names (from the table) in reverse order (last to first).

Hints:
- Use the sqlite3 module in Python
- Use SQL's WHERE clause for department filtering
- Use Python's reversed() or slicing for reverse order

Rubric:
- Table created: 20%
- Records inserted: 20%
- Select and update: 30%
- Python reverse print: 30%
"""