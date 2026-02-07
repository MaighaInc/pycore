"""
Beginner Assignment 3: BMI Calculator

Scenario:
A fitness app needs to calculate Body Mass Index (BMI) for users.

Objective:
Create a function that calculates BMI and returns the category.

Tasks:
1. Define a function calculate_bmi(weight_kg, height_m) that returns BMI
2. Define a function get_bmi_category(bmi) that returns the category string
3. Test with the provided user data
4. Print results with BMI value and category

BMI Formula:
- BMI = weight (kg) / (height (m))²

Categories:
- Below 18.5: Underweight
- 18.5 to 24.9: Normal weight
- 25.0 to 29.9: Overweight
- 30.0 and above: Obese

Inputs:
- User 1: weight = 70 kg, height = 1.75 m
- User 2: weight = 85 kg, height = 1.80 m

Expected Output:
User 1: BMI = 22.86 (Normal weight)
User 2: BMI = 26.23 (Overweight)

Hints:
- Use ** for power (height**2)
- Use if/elif/else for categories
- Round BMI to 2 decimals

Rubric:
- Correct BMI calculation: 30%
- Correct category function: 30%
- Proper logic flow: 20%
- Formatted output: 20%
"""

# Input data
users = [
    ("User 1", 70, 1.75),
    ("User 2", 85, 1.80)
]

# Your code here

