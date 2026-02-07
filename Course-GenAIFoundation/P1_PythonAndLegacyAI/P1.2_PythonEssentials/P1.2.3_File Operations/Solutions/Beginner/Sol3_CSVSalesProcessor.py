"""
Solution: Beginner Assignment 3 - CSV Sales Processor
"""

import csv

# Input data
sales = [
    ("2026-02-01", "Laptop", 2, 1200.00),
    ("2026-02-02", "Mouse", 5, 25.00),
    ("2026-02-03", "Keyboard", 3, 75.00)
]

filename = "sales.csv"

# Write CSV
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "product", "quantity", "price"])
    writer.writerows(sales)

# Read CSV
with open(filename, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
