"""
Solution: Beginner Assignment 2 - Discount Calculator
"""

# Input data
products = [
    ("Product A", 100, 20),
    ("Product B", 250, 15),
    ("Product C", 50, 10)
]

# Function definition
def calculate_discount(price, discount_percent):
    """Calculate final price after applying discount"""
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

# Process each product
for name, price, discount in products:
    final = calculate_discount(price, discount)
    print(f"{name}: ${price:.2f} - {discount}% discount = ${final:.2f}")
