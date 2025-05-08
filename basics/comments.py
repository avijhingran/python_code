# --- Single-line Comment ---
# This script calculates user discounts based on membership level

# --- Inline Comment ---
membership_level = "Gold"  # User's membership category

# --- Multi-line Comments (using multiple #) ---
# Step 1: Define base discount percentages
# Step 2: Apply extra benefits if applicable
# Step 3: Display final discount

# Dictionary holding base discounts
discounts = {
    "Silver": 5,
    "Gold": 10,
    "Platinum": 15
}

# --- Function with Docstring ---
def calculate_discount(level):
    """
    Calculates discount based on the membership level.
    
    Args:
    level (str): Membership category ('Silver', 'Gold', 'Platinum')
    
    Returns:
    int: Discount percentage
    """
    return discounts.get(level, 0)  # Default to 0 if level not found

# --- Multi-line String Used as Comment ---
"""
The following code fetches the discount for the user.
If the user's level is not recognized, no discount is applied.
"""

# Get the discount for the current user
user_discount = calculate_discount(membership_level)

# Output
print(f"Hello {membership_level} member! You get a {user_discount}% discount.")
