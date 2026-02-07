"""
Solution: Intermediate Assignment 2 - Discount Calculator
"""

# Input data
cart = [
    ("Shoes", 120, 15, "SAVE10"),
    ("Jacket", 200, 20, None),
    ("Socks", 25, 0, "SAVE25"),
    ("Hat", 40, 5, "SAVE10")
]

# Helper functions
def calculate_discount(price, discount_percent=0):
    """Apply percentage discount to a price."""
    return price * (1 - discount_percent / 100)

def apply_coupon(price, coupon_code=None):
    """Apply coupon discount if valid."""
    coupons = {
        "SAVE10": 10,
        "SAVE25": 25
    }
    if coupon_code in coupons:
        return price * (1 - coupons[coupon_code] / 100)
    return price

def final_price(price, discount_percent=0, coupon_code=None):
    """Apply base discount then coupon discount."""
    discounted = calculate_discount(price, discount_percent)
    return apply_coupon(discounted, coupon_code)

# Process cart
total = 0
for name, price, discount, coupon in cart:
    final = final_price(price, discount, coupon)
    total += final
    print(f"{name}: ${price:.2f} -> ${final:.2f}")

print(f"\nTotal: ${total:.2f}")
