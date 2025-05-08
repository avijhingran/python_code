# Type 1: Without passing, without returning
def greet():
    print("Hello, welcome!")

greet()

# Type 2: With passing, without returning
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")

# Type 3: Without passing, with returning
def get_default_username():
    return "GuestUser"

user = get_default_username()
print(user)

# Type 4: With passing, with returning
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(result)

# Type 5: Returning Multiple Values
def get_user_details():
    name = "Alice"
    age = 30
    return name, age  # Returns a tuple

user_name, user_age = get_user_details()
print(user_name, user_age)

# Type 6: Pass by reference
def add_item(my_list):
    my_list.append("New Item")
    print("Inside function:", my_list)

shopping_list = ["Milk", "Bread"]
add_item(shopping_list)
print("Outside function:", shopping_list)

# Type 7: Return by reference
def create_shopping_list():
    items = ["Eggs", "Flour", "Sugar"]
    return items

new_list = create_shopping_list()
new_list.append("Butter")
print(new_list)

# Type 8: Anonymous Functions
square = lambda x: x * x
print(square(5))  # Output: 25

# Type 9: Variable Positional Arguments (*args)
def add_numbers(*args):
    print(args)  # args is a tuple
    return sum(args)

result = add_numbers(2, 4, 6, 8)
print("Sum:", result)

# Type 10: Variable Keyword Arguments (**kwargs)
def print_user_info(**kwargs):
    print(kwargs)  # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=30, city="New York")
