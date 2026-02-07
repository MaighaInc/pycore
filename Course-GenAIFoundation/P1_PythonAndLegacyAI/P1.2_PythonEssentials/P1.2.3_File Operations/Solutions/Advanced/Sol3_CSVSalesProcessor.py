"""
Solution: Advanced Assignment 3 - CSV Sales Processor
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

# Write sales.csv
with open("sales.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "salesperson", "product", "quantity", "price"])
    writer.writerows(sales)

revenue_by_product = {}
revenue_by_person = {}

# Read and aggregate
with open("sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        person = row["salesperson"]
        quantity = int(row["quantity"])
        price = float(row["price"])
        revenue = quantity * price

        revenue_by_product[product] = revenue_by_product.get(product, 0) + revenue
        revenue_by_person[person] = revenue_by_person.get(person, 0) + revenue

# Write product summary
with open("sales_by_product.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["product", "revenue"])
    for product, revenue in revenue_by_product.items():
        writer.writerow([product, revenue])

# Write person summary
with open("sales_by_person.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["salesperson", "revenue"])
    for person, revenue in revenue_by_person.items():
        writer.writerow([person, revenue])

# Print top results
top_product = max(revenue_by_product, key=revenue_by_product.get)
top_person = max(revenue_by_person, key=revenue_by_person.get)

print(f"Top Product: {top_product} (${revenue_by_product[top_product]:.2f})")
print(f"Top Salesperson: {top_person} (${revenue_by_person[top_person]:.2f})")
