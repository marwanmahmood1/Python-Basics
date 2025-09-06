# =========================
#           SETS
# =========================
# A Set is an unordered collection of UNIQUE elements.
# - No duplicates allowed
# - Elements are not indexed (you can't access by position)

# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}
print("Fruits set:", fruits)  # Duplicate "apple" is removed

# Adding and removing elements
fruits.add("orange")
fruits.remove("banana")  # KeyError if "banana" not found
fruits.discard("pear")   # Safe remove (no error if missing)
print("Updated fruits:", fruits)

# Checking membership
print("Is apple in fruits?", "apple" in fruits)

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)        # {1, 2, 3, 4, 5, 6}
print("Intersection:", A & B) # {3, 4}
print("Difference:", A - B)   # {1, 2}
print("Symmetric Diff:", A ^ B)  # {1, 2, 5, 6}
