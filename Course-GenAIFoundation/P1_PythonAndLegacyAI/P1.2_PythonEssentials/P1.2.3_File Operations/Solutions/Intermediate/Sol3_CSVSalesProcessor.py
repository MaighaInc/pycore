"""
Solution: Intermediate Assignment 3 - CSV Sales Processor
"""

import csv

# Input data
sales = [
    ("2026-02-01", "Laptop", 2, 1200.00),
    ("2026-02-02", "Mouse", 5, 25.00),
    ("2026-02-03", "Keyboard", 3, 75.00),
    ("2026-02-04", "Mouse", 2, 25.00)
]

# Write sales.csv
with open("sales.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "product", "quantity", "price"])
    writer.writerows(sales)

# Read and aggregate
revenue_by_product = {}
with open("sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])
        price = float(row["price"])
        revenue = quantity * price
        revenue_by_product[product] = revenue_by_product.get(product, 0) + revenue

# Write summary
with open("sales_summary.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["product", "revenue"])
    for product, revenue in revenue_by_product.items():
        writer.writerow([product, revenue])

# Print summary
for product, revenue in revenue_by_product.items():
    print(f"{product}: {revenue}")
