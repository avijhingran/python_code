import os

filename = "demo_file.txt"

# 1. Write (creates or overwrites)
with open(filename, "w") as f:
    f.write("L
    f.write("Line 2: This is a test file.\n")

# 2. Append (adds without erasing)
with open(filename, "a") as f:
    f.write("Line 3: Appending new content.\n")

# 3. Read entire file
with open(filename, "r") as f:
    content = f.read()
    print("Full content:\n", content)

# 4. Read line-by-line
print("\n Reading line-by-line:")
with open(filename, "r") as f:
    for line in f:
        print(line.strip())

# 5. Read specific characters + seek
print("\n Partial read and seek:")
with open(filename, "r") as f:
    print("First 10 chars:", f.read(10))
    f.seek(0)  # Reset to beginning
    print("After seek, first line:", f.readline().strip())

# 6. Check if file exists before deleting (cleanup)
if os.path.exists(filename):
    os.remove(filename)
    print(f"\n '{filename}' deleted after demo.")
else:
    print("File not found.")
