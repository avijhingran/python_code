# 1. for loop (simple)
print("\n--- 1. for loop ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. while loop
print("\n--- 2. while loop ---")
count = 0
while count < 5:
    print(count)
    count += 1

# 3. Nested for loop
print("\n--- 3. Nested for loop ---")
for row in range(2):
    for col in range(3):
        print(f"Row {row}, Column {col}")

# 4. break inside a loop
print("\n--- 4. break inside for loop ---")
numbers = [1, 3, 7, 9, 11]
for number in numbers:
    if number == 7:
        print("Found 7!")
        break
    print(f"Checked {number}")

# 5. continue inside a loop
print("\n--- 5. continue inside for loop ---")
for num in range(1, 8):
    if num == 5:
        continue
    print(num)

# 6. pass inside a loop
print("\n--- 6. pass inside for loop ---")
for task in ["backup", "update", "monitor"]:
    pass  # Placeholder for future implementation

# 7. for-else loop
print("\n--- 7. for-else loop ---")
items = ["pen", "pencil", "eraser"]
for item in items:
    if item == "marker":
        print("Marker found!")
        break
else:
    print("Marker not found.")

# 8. while-else loop
print("\n--- 8. while-else loop ---")
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted.")
        break
    attempts += 1
else:
    print("Account locked. Too many failed attempts.")
