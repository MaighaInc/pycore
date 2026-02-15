"""
Assignment 2: Feedback Collector with Advanced Filtering and Batch Delete (Advanced)

Scenario:
You are building an advanced feedback collector. In addition to filtering and counting, users can now filter feedback by multiple keywords (case-insensitive), perform batch delete of selected feedback entries, and benefit from improved feedback display and error handling.

Objective:
- Implement advanced filtering (multi-keyword, case-insensitive)
- Allow batch deletion of selected feedback entries
- Improve feedback display and error handling
- Maintain all previous features (add, filter, count, reverse order)

Tasks:
1. Add a filter box that allows searching feedback messages by multiple keywords (case-insensitive, matches if any keyword is present).
2. Allow users to select multiple feedback entries and delete them in one action.
3. Display clear error and success messages for all operations, including batch actions and invalid input.
4. Keep all previous features (add, filter, count, reverse order).

Hints:
- Use SQL's LIKE operator for filtering with multiple keywords
- Use checkboxes in the feedback list for batch selection
- Use Flask's flash() for user feedback
- Use Jinja2 to display messages and update the feedback list

Rubric:
- Advanced filtering logic: 30%
- Batch delete implementation: 25%
- Error handling and feedback: 25%
- Code clarity and comments: 20%
"""