"""
Mini Project 3: Async Sales Dashboard
Level: Intermediate

Concepts Used:
- CSV processing
- Functions and aggregation
- Async programming (concurrent processing)
- Error handling for file ops

Description:
Create a sales dashboard that writes CSV data, reads it asynchronously,
computes summaries, and writes a report.

Expected Output (sample):
==================================================
ASYNC SALES DASHBOARD
==================================================
Total transactions: 5
Top Product: Laptop ($3600.00)
Top Salesperson: Alice ($2750.00)
Report saved to: sales_report.txt
==================================================
"""

import asyncio
import csv

# Sales data - DO NOT MODIFY
sales = [
    ("2026-02-01", "Alice", "Laptop", 2, 1200.00),
    ("2026-02-01", "Bob", "Mouse", 5, 25.00),
    ("2026-02-02", "Alice", "Monitor", 1, 350.00),
    ("2026-02-03", "Carol", "Keyboard", 3, 75.00),
    ("2026-02-03", "Bob", "Laptop", 1, 1200.00)
]

print("=" * 50)
print("ASYNC SALES DASHBOARD")
print("=" * 50)

# TODO: Step 1 - Write sales.csv

# TODO: Step 2 - Read CSV asynchronously (use asyncio.to_thread)

# TODO: Step 3 - Compute revenue by product and by salesperson

# TODO: Step 4 - Write report to sales_report.txt

# TODO: Step 5 - Orchestrate steps in async main()

# YOUR CODE HERE

