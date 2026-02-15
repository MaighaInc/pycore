"""
Intermediate Assignment 4: Contact Form with Validation

Scenario:
Enhance your contact form to validate that both name and message are provided. If either is missing, show an error message on the form page using a template.

Objective:
- Validate form input on POST
- Show error message if fields are missing
- Show thank you message if valid

Tasks:
1. Use a `contact.html` template for the form and error display
2. On POST, check if name and message are filled
3. If not, re-render the form with an error message
4. If valid, show thank you message

Hints:
- Use request.form and pass error to template
- Use Jinja to conditionally display error

Rubric:
- Validation and error display work: 40%
- Uses templates and variables: 40%
- Code clarity and comments: 20%
"""

# Your code here
