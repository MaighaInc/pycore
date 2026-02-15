"""
Assignment 1: Contact Book with Advanced Search and Error Handling (Advanced)

Scenario:
You are building an advanced contact book. In addition to all previous features, users can now perform advanced searches (by name, email, or phone, with partial matches) and benefit from improved error handling and user feedback.

Objective:
- Implement advanced search (multi-field, partial match)
- Improve error handling and user feedback for all operations
- Maintain all previous features (add, search, edit, delete, duplicate prevention, messages)

Tasks:
1. Add a search form that allows searching contacts by name, email, or phone (partial match, case-insensitive).
2. Display clear error and success messages for all operations, including invalid input.
3. Keep all previous features (add, search, edit, delete, duplicate prevention, messages).

Hints:
- Use SQL's LIKE operator for partial, case-insensitive search across multiple fields
- Use Flask's flash() for user feedback
- Use Jinja2 to display messages and update the contact list

Rubric:
- Advanced search logic: 40%
- Error handling and feedback: 30%
- Add/edit/delete/duplicate logic: 30%
"""