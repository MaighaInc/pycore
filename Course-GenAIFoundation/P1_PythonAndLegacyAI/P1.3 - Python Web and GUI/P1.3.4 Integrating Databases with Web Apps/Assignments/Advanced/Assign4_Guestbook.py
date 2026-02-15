"""
Assignment 4: Guestbook with Advanced Search, Batch Delete, and Pagination (Advanced)

Scenario:
You are building an advanced guestbook. In addition to editing, deleting, and pagination, users can now search entries by multiple keywords (case-insensitive), perform batch delete of selected entries, and benefit from improved pagination and error handling.

Objective:
- Implement advanced search (multi-keyword, case-insensitive)
- Allow batch deletion of selected guestbook entries
- Improve pagination and error handling
- Maintain all previous features (edit, delete, pagination)

Tasks:
1. Add a search box to filter guestbook entries by multiple keywords (case-insensitive, matches if any keyword is present).
2. Allow users to select multiple guestbook entries and delete them in one action.
3. Implement improved pagination (e.g., show total entries, current/total pages, navigation links).
4. Display clear error and success messages for all operations, including batch actions and invalid input.
5. Keep all previous features (edit, delete, pagination).

Hints:
- Use SQL's LIKE operator for filtering with multiple keywords
- Use checkboxes in the guestbook list for batch selection
- Use Flask's flash() for user feedback
- Use Jinja2 to display messages and update the guestbook list

Rubric:
- Advanced search logic: 30%
- Batch delete implementation: 25%
- Pagination and feedback: 25%
- Code clarity and comments: 20%
"""