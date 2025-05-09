import copy

original = [[1, 2], [3, 4]]

# 1. Assignment
assigned = original
# Modify outer list
assigned.append(["assigned"])
print("After Assignment (Modifying outer list):")
print("Original:", original)
print("Assigned:", assigned)
print()
# Modify inner list
assigned[0][0] = 100     # affects original, assigned, and shallow
print("After Assignment (Modifying inner list):")
print("Original:", original)
print("Assigned:", assigned)
print()

# 2. Shallow Copy
shallow = copy.copy(original)
# Modify outer list
shallow.append(["shallow"])     # does NOT affect original
print("After Shallow Copy (Modifying outer list):")
print("Original:", original)
print("Assigned:", assigned)
print("Shallow:", shallow)
print()
# Modify inner list
shallow[0][1] = 200       # affects original, assigned, and shallow
assigned[0][0] = 1000     # affects original, assigned, and shallow
print("After Shallow Copy (Modifying inner list):")
print("Original:", original)
print("Assigned:", assigned)
print("Shallow:", shallow)
print()

# 3. Deep Copy
deep = copy.deepcopy(original)
# Modify outer list
deep.append(["deep"])     # does NOT affect original
print("After Deep Copy (Modifying outer list):")
print("Original:", original)
print("Assigned:", assigned)
print("Shallow:", shallow)
print("Deep:", deep)
print()
# Modify inner list
deep[1][0] = 300          # does NOT affect original
print("After Deep Copy (Modifying inner list):")
print("Original:", original)
print("Assigned:", assigned)
print("Shallow:", shallow)
print("Deep:", deep)
