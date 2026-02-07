"""
Mini Project 3: Async Sales Dashboard (Solution)
"""

import asyncio
import csv

sales = [
    ("2026-02-01", "Alice", "Laptop", 2, 1200.00),
    ("2026-02-01", "Bob", "Mouse", 5, 25.00),
    ("2026-02-02", "Alice", "Monitor", 1, 350.00),
    ("2026-02-03", "Carol", "Keyboard", 3, 75.00),
    ("2026-02-03", "Bob", "Laptop", 1, 1200.00)
]

def write_sales_csv(filename, rows):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "salesperson", "product", "quantity", "price"])
        writer.writerows(rows)

def read_sales_csv(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def compute_summaries(rows):
    revenue_by_product = {}
    revenue_by_person = {}
    for row in rows:
        product = row["product"]
        person = row["salesperson"]
        quantity = int(row["quantity"])
        price = float(row["price"])
        revenue = quantity * price
        revenue_by_product[product] = revenue_by_product.get(product, 0) + revenue
        revenue_by_person[person] = revenue_by_person.get(person, 0) + revenue
    return revenue_by_product, revenue_by_person

def write_report(filename, total, top_product, top_person):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Total transactions: {total}\n")
        file.write(f"Top Product: {top_product[0]} (${top_product[1]:.2f})\n")
        file.write(f"Top Salesperson: {top_person[0]} (${top_person[1]:.2f})\n")

async def main():
    print("=" * 50)
    print("ASYNC SALES DASHBOARD")
    print("=" * 50)

    await asyncio.to_thread(write_sales_csv, "sales.csv", sales)
    rows = await asyncio.to_thread(read_sales_csv, "sales.csv")

    revenue_by_product, revenue_by_person = compute_summaries(rows)

    top_product = max(revenue_by_product.items(), key=lambda x: x[1])
    top_person = max(revenue_by_person.items(), key=lambda x: x[1])

    print(f"Total transactions: {len(rows)}")
    print(f"Top Product: {top_product[0]} (${top_product[1]:.2f})")
    print(f"Top Salesperson: {top_person[0]} (${top_person[1]:.2f})")

    write_report("sales_report.txt", len(rows), top_product, top_person)
    print("Report saved to: sales_report.txt")
    print("=" * 50)

asyncio.run(main())
