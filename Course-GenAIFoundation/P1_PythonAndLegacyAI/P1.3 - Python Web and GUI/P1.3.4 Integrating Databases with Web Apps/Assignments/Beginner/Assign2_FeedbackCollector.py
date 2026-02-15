"""
Assignment 2: Feedback Collector - Add and List (Beginner)

Scenario:
You are creating a simple feedback collector web app where users can submit feedback through a form. The app displays all feedback entries.

Objective:
- Set up a Flask app with SQLite
- Create a table for feedback
- Build a web form to collect feedback
- Display all feedback entries

Tasks:
1. Create a Flask app and connect it to a SQLite database called 'feedback.db'.
2. Create a table 'feedback' with columns: id (INTEGER PRIMARY KEY), message (TEXT).
3. Build a web form (HTML) to submit feedback messages.
4. Store submitted feedback in the database.
5. Display all feedback messages on a web page using a template.

Hints:
- Use Flask's render_template, request, and g for database connection
- Use sqlite3 for database operations
- Use Jinja2 templating to display feedback

Rubric:
- Flask app and database setup: 30%
- Web form and data storage: 30%
- Displaying feedback: 30%
- Code clarity and comments: 10%
"""