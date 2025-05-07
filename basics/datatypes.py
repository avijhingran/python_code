# --- Variable Examples with Different Data Types ---

# int: number of products user purchased
products_purchased = 5

# float: user's account balance in dollars
account_balance = 245.75

# string: user's full name
full_name = "Alex Johnson"

# list: user's favorite categories
favorite_categories = ["Electronics", "Books", "Fitness"]

# dict: complete user profile
user_profile = {
    "name": full_name,
    "purchases": products_purchased,
    "balance": account_balance,
    "favorites": favorite_categories,
    "location": (40.7128, -74.0060),   # tuple: user's (latitude, longitude)
    "is_premium_member": True
}

# tuple: coordinates of user's last login location (immutable)
last_login_coordinates = (37.7749, -122.4194)

# set: unique coupons used by the user
used_coupons = {"WELCOME10", "SUMMER20", "WELCOME10"}  # duplicates auto-removed

# --- Printing all information ---
print("User Profile Details:\n")
print(f"Name: {user_profile['name']}")
print(f"Products Purchased: {user_profile['purchases']}")
print(f"Account Balance: ${user_profile['balance']}")
print(f"Favorite Categories: {', '.join(user_profile['favorites'])}")
print(f"Location: {user_profile['location']}")
print(f"Premium Member: {user_profile['is_premium_member']}")
print(f"Last Login Coordinates: {last_login_coordinates}")
print(f"Coupons Used (Unique): {used_coupons}")
