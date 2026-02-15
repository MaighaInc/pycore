"""
Assignment 3: Task Tracker - Add and List (Beginner)

Scenario:
You are building a simple web-based task tracker where users can add tasks and view all tasks.

Objective:
- Set up a Flask app with SQLite
- Create a table for tasks
- Build a web form to add tasks
- Display all tasks on a web page

Tasks:
1. Create a Flask app and connect it to a SQLite database called 'tasks.db'.
2. Create a table 'tasks' with columns: id (INTEGER PRIMARY KEY), description (TEXT).
3. Build a web form (HTML) to add a new task (description).
4. Store submitted tasks in the database.
5. Display all tasks on a web page using a template.

Hints:
- Use Flask's render_template, request, and g for database connection
- Use sqlite3 for database operations
- Use Jinja2 templating to display tasks

Rubric:
- Flask app and database setup: 30%
- Web form and data storage: 30%
- Displaying tasks: 30%
- Code clarity and comments: 10%
"""