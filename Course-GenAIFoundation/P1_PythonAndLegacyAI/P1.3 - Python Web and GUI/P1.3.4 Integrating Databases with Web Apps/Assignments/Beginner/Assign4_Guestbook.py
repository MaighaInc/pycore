"""
Assignment 4: Guestbook - Add and List (Beginner)

Scenario:
You are creating a simple web-based guestbook where visitors can sign their name and leave a message. All entries are displayed on the page.

Objective:
- Set up a Flask app with SQLite
- Create a table for guestbook entries
- Build a web form to sign the guestbook
- Display all guestbook entries on a web page

Tasks:
1. Create a Flask app and connect it to a SQLite database called 'guestbook.db'.
2. Create a table 'entries' with columns: id (INTEGER PRIMARY KEY), name (TEXT), message (TEXT).
3. Build a web form (HTML) to add a new entry (name and message).
4. Store submitted entries in the database.
5. Display all guestbook entries on a web page using a template.

Hints:
- Use Flask's render_template, request, and g for database connection
- Use sqlite3 for database operations
- Use Jinja2 templating to display entries

Rubric:
- Flask app and database setup: 30%
- Web form and data storage: 30%
- Displaying entries: 30%
- Code clarity and comments: 10%
"""