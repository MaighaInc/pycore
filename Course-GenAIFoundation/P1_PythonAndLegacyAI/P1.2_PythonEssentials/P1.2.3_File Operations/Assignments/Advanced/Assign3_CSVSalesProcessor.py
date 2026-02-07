"""
Advanced Assignment 3: CSV Sales Processor

Scenario:
Generate multi-dimensional sales summaries from CSV data.

Objective:
Create product and salesperson summaries, then write two summary CSVs.

Tasks:
1. Write sales data to "sales.csv"
2. Read CSV and compute:
   - revenue by product
   - revenue by salesperson
3. Write "sales_by_product.csv" and "sales_by_person.csv"
4. Print the top product and top salesperson

Inputs:
sales = [
    ("2026-02-01", "Alice", "Laptop", 2, 1200.00),
    ("2026-02-01", "Bob", "Mouse", 5, 25.00),
    ("2026-02-02", "Alice", "Monitor", 1, 350.00),
    ("2026-02-03", "Carol", "Keyboard", 3, 75.00),
    ("2026-02-03", "Bob", "Laptop", 1, 1200.00)
]

Expected Output (sample):
Top Product: Laptop ($3600.00)
Top Salesperson: Alice ($2750.00)

Hints:
- Use csv.DictReader
- Use dict accumulators

Rubric:
- Correct aggregation: 40%
- Correct CSV outputs: 30%
- Output formatting: 30%
"""

import csv

# Input data
sales = [
    ("2026-02-01", "Alice", "Laptop", 2, 1200.00),
    ("2026-02-01", "Bob", "Mouse", 5, 25.00),
    ("2026-02-02", "Alice", "Monitor", 1, 350.00),
    ("2026-02-03", "Carol", "Keyboard", 3, 75.00),
    ("2026-02-03", "Bob", "Laptop", 1, 1200.00)
]

# Your code here

