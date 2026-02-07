"""
Advanced Assignment 3: BMI Calculator

Scenario:
A health analytics tool needs BMI calculations plus summary analytics.

Objective:
Build a processing pipeline using higher-order functions.

Tasks:
1. Create functions to compute BMI and category
2. Create pipeline functions to:
   - Transform user records to BMI records
   - Filter by category
   - Aggregate statistics (avg BMI per category)
3. Provide a reusable summarize_bmi(records, *, group_by_category=True)
4. Print a report

Inputs:
users = [
    {"name": "Ava", "weight": 70, "height": 1.75, "unit": "metric"},
    {"name": "Liam", "weight": 180, "height": 70, "unit": "imperial"},
    {"name": "Noah", "weight": 95, "height": 1.82, "unit": "metric"},
    {"name": "Mia", "weight": 50, "height": 1.62, "unit": "metric"}
]

Expected Output (sample):
BMI Report
==========
Ava: 22.86 (Normal weight)
Liam: 25.82 (Overweight)
Noah: 28.68 (Overweight)
Mia: 19.05 (Normal weight)

Category Averages:
Normal weight: 20.96
Overweight: 27.25

Hints:
- Use list comprehensions for transforms
- Use dict for aggregation
- Round averages to 2 decimals

Rubric:
- Correct BMI computation: 30%
- Correct grouping/aggregation: 30%
- Clean pipeline design: 20%
- Output formatting: 20%
"""

# Input data
users = [
    {"name": "Ava", "weight": 70, "height": 1.75, "unit": "metric"},
    {"name": "Liam", "weight": 180, "height": 70, "unit": "imperial"},
    {"name": "Noah", "weight": 95, "height": 1.82, "unit": "metric"},
    {"name": "Mia", "weight": 50, "height": 1.62, "unit": "metric"}
]

# Your code here

