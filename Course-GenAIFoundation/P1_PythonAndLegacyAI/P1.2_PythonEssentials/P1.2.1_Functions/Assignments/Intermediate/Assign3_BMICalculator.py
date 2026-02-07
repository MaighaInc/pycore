"""
Intermediate Assignment 3: BMI Calculator

Scenario:
A fitness platform receives user data in mixed units and needs consistent
BMI calculations and categories.

Objective:
Create functions that support metric and imperial units.

Tasks:
1. Define bmi_metric(weight_kg, height_m)
2. Define bmi_imperial(weight_lb, height_in)
3. Define get_bmi_category(bmi)
4. Process multiple users and print results

Inputs:
users = [
    {"name": "Ava", "weight": 70, "height": 1.75, "unit": "metric"},
    {"name": "Liam", "weight": 180, "height": 70, "unit": "imperial"},
    {"name": "Noah", "weight": 95, "height": 1.82, "unit": "metric"}
]

Expected Output:
Ava: BMI = 22.86 (Normal weight)
Liam: BMI = 25.82 (Overweight)
Noah: BMI = 28.68 (Overweight)

Hints:
- Imperial BMI: (weight_lb / height_in^2) * 703
- Use helper functions for readability
- Round BMI to 2 decimals

Rubric:
- Correct BMI formulas: 40%
- Correct category logic: 30%
- Proper function usage: 20%
- Output formatting: 10%
"""

# Input data
users = [
    {"name": "Ava", "weight": 70, "height": 1.75, "unit": "metric"},
    {"name": "Liam", "weight": 180, "height": 70, "unit": "imperial"},
    {"name": "Noah", "weight": 95, "height": 1.82, "unit": "metric"}
]

# Your code here

