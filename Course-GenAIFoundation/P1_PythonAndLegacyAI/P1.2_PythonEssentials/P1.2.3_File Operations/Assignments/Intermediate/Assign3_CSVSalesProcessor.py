"""
Intermediate Assignment 3: CSV Sales Processor

Scenario:
Summarize sales data from CSV and create a summary CSV.

Objective:
Practice CSV reading, aggregation, and writing.

Tasks:
1. Write sales data to "sales.csv"
2. Read the CSV and compute total revenue per product
3. Write summary to "sales_summary.csv" with columns: product, revenue
4. Print summary rows

Inputs:
sales = [
    ("2026-02-01", "Laptop", 2, 1200.00),
    ("2026-02-02", "Mouse", 5, 25.00),
    ("2026-02-03", "Keyboard", 3, 75.00),
    ("2026-02-04", "Mouse", 2, 25.00)
]

Expected Output:
Laptop: 2400.0
Mouse: 175.0
Keyboard: 225.0

Hints:
- Revenue = quantity * price
- Use csv.DictReader and DictWriter for clarity

Rubric:
- Correct aggregation: 40%
- Correct CSV writing: 30%
- Output formatting: 30%
"""

import csv

# Input data
sales = [
    ("2026-02-01", "Laptop", 2, 1200.00),
    ("2026-02-02", "Mouse", 5, 25.00),
    ("2026-02-03", "Keyboard", 3, 75.00),
    ("2026-02-04", "Mouse", 2, 25.00)
]

# Your code here

