"""
Assignment 3: Task Tracker with Advanced Filtering and Batch Update (Advanced)

Scenario:
You are building an advanced task tracker. In addition to previous features, users can now filter tasks by multiple criteria (due date range, completion status, keyword), perform batch updates (e.g., mark multiple tasks as completed), and benefit from improved overdue logic and error handling.

Objective:
- Implement advanced filtering (due date range, completion status, keyword)
- Allow batch update of selected tasks (e.g., mark as completed)
- Improve overdue logic and error handling
- Maintain all previous features (due dates, completion filter, overdue highlighting)

Tasks:
1. Add filters to search tasks by due date range, completion status, and keyword in the task description (all filters can be combined).
2. Allow users to select multiple tasks and mark them as completed in one action.
3. Highlight overdue tasks and display clear error/success messages for all operations.
4. Keep all previous features (due dates, completion filter, overdue highlighting).

Hints:
- Use SQL WHERE for combining multiple filters
- Use checkboxes in the task list for batch selection
- Use Flask's flash() for user feedback
- Use Jinja2 to display messages and update the task list

Rubric:
- Advanced filtering logic: 30%
- Batch update implementation: 25%
- Overdue logic and feedback: 25%
- Code clarity and comments: 20%
"""