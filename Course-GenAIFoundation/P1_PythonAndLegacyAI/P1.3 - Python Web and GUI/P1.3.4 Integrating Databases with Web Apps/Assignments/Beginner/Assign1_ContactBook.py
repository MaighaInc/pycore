"""
Assignment 1: Contact Book - Add and List (Beginner)

Scenario:
You are building a simple web-based contact book using Flask and SQLite. Users can add contacts and view all contacts.

Objective:
- Set up a Flask app connected to SQLite
- Create a table for storing contacts
- Build a web form to add contacts
- Display all contacts on a web page

Tasks:
1. Create a Flask app and connect it to a SQLite database called 'contacts.db'.
2. Create a table 'contacts' with columns: id (INTEGER PRIMARY KEY), name (TEXT), email (TEXT).
3. Build a web form (HTML) to add a new contact (name and email).
4. Store submitted form data in the database.
5. Display all contacts on a web page using a template.

Hints:
- Use Flask's render_template, request, and g for database connection
- Use sqlite3 for database operations
- Use Jinja2 templating to display contacts

Rubric:
- Flask app and database setup: 30%
- Web form and data storage: 30%
- Displaying contacts: 30%
- Code clarity and comments: 10%
"""