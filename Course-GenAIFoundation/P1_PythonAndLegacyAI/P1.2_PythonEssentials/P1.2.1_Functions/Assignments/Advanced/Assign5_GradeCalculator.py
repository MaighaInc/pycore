"""
Advanced Assignment 5: Grade Calculator

Scenario:
A gradebook system needs flexible grading rules including dropping the
lowest score and applying a curve.

Objective:
Create a grading pipeline using reusable functions.

Tasks:
1. Create drop_lowest(scores) that removes one lowest score
2. Create apply_curve(scores, curve_points)
3. Create calculate_final(scores, weights=None, drop=False, curve=0)
4. Create grade_report(student_records) that prints final grades

Inputs:
students = [
    ("Maya", [92, 85, 88, 90], [0.3, 0.2, 0.2, 0.3]),
    ("Ethan", [75, 80, 70, 68], [0.4, 0.2, 0.2, 0.2]),
    ("Zoe", [98, 95, 100, 92], [0.2, 0.3, 0.3, 0.2])
]

Expected Output (sample):
Maya: Final 90.1 = Grade A
Ethan: Final 74.0 = Grade C
Zoe: Final 98.6 = Grade A

Hints:
- Use optional args to enable drop/curve
- Keep grading logic in helper functions
- Reuse get_letter_grade from previous levels

Rubric:
- Correct drop/curve logic: 35%
- Correct weighted calculation: 30%
- Clean function composition: 20%
- Output formatting: 15%
"""

# Input data
students = [
    ("Maya", [92, 85, 88, 90], [0.3, 0.2, 0.2, 0.3]),
    ("Ethan", [75, 80, 70, 68], [0.4, 0.2, 0.2, 0.2]),
    ("Zoe", [98, 95, 100, 92], [0.2, 0.3, 0.3, 0.2])
]

# Your code here

