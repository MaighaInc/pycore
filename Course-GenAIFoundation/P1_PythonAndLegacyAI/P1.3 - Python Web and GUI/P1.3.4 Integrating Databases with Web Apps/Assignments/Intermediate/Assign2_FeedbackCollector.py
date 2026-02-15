"""
Assignment 2: Feedback Collector - Add, List, Filter (Intermediate)

Scenario:
You are improving your feedback collector app. In addition to adding and listing feedback, users can now filter feedback messages by keyword, and the most recent feedback appears first.

Objective:
- Add, list, and filter feedback using Flask and SQLite
- Show feedback in reverse chronological order
- Use templates for all HTML rendering

Tasks:
1. Add a search/filter box to filter feedback messages by keyword (case-insensitive).
2. Display only feedback messages that match the filter, with the most recent first.
3. Keep the ability to add new feedback messages.

Hints:
- Use SQL's LIKE operator for filtering
- Use ORDER BY id DESC to show most recent first
- Use Jinja2 templating to display feedback and filter box

Rubric:
- Filtering logic: 40%
- Add/list logic: 40%
- Code clarity and comments: 20%
"""