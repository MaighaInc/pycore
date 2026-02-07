"""
Intermediate Assignment 5: Grade Calculator

Scenario:
Compute final grades from multiple assessments with configurable weights.

Objective:
Create functions that calculate weighted averages and letter grades.

Tasks:
1. Define calculate_weighted_average(scores, weights)
2. Define get_letter_grade(score)
3. Process each student record and print results

Inputs:
students = [
    ("Maya", [92, 85, 88], [0.4, 0.3, 0.3]),
    ("Ethan", [75, 80, 70], [0.5, 0.2, 0.3]),
    ("Zoe", [98, 95, 100], [0.3, 0.3, 0.4])
]

Expected Output:
Maya: Final 88.6 = Grade B
Ethan: Final 74.5 = Grade C
Zoe: Final 98.5 = Grade A

Hints:
- Multiply each score by its weight and sum
- Use zip(scores, weights)
- Reuse get_letter_grade from beginner

Rubric:
- Correct weighted average: 40%
- Correct grading logic: 30%
- Proper function usage: 20%
- Output formatting: 10%
"""

# Input data
students = [
    ("Maya", [92, 85, 88], [0.4, 0.3, 0.3]),
    ("Ethan", [75, 80, 70], [0.5, 0.2, 0.3]),
    ("Zoe", [98, 95, 100], [0.3, 0.3, 0.4])
]

# Your code here

