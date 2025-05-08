# Example Variables
user_role = "Premium"
age = 17
is_logged_in = True

# 1. Simple if
if is_logged_in:
    print("User is logged in.")

# 2. if-else
if age >= 18:
    print("User is an adult.")
else:
    print("User is a minor.")

# 3. if-elif-else
if user_role == "Admin":
    print("Access to Admin Dashboard.")
elif user_role == "Premium":
    print("Access to Premium Features.")
elif user_role == "Basic":
    print("Access to Basic Features.")
else:
    print("Guest access only.")

# 4. Nested if
if is_logged_in:
    if user_role == "Admin":
        print("Admin can manage users.")

# 5. Ternary (One-Line if-else)
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# 6. Match-case (Python 3.10+ feature)
# If you're using Python 3.10 or higher
match user_role:
    case "Admin":
        print("Matched: Admin role detected.")
    case "Premium":
        print("Matched: Premium user detected.")
    case "Basic":
        print("Matched: Basic user detected.")
    case _:
        print("Matched: Unknown user type.")
