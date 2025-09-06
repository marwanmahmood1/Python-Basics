# =========================
#          LISTS
# =========================
# A list is a collection of items stored in a single variable.
# Lists are ordered, mutable (can be changed), and allow duplicate values.

# Creating a list:
fruits = ["apple", "banana", "cherry", "banana"]
print("Fruits list:", fruits)

# Accessing items:
print("First fruit:", fruits[0])    # apple
print("Last fruit:", fruits[-1])    # banana

# Modifying a list:
fruits[1] = "blueberry"
print("After modification:", fruits)

# Adding items:
fruits.append("orange")     # Add to the end
fruits.insert(1, "kiwi")    # Insert at a specific index
print("After adding items:", fruits)

# Removing items:
fruits.remove("banana")     # Removes the first occurrence of "banana"
popped_item = fruits.pop()  # Removes the last item
print("After removing items:", fruits)
print("Popped item:", popped_item)

# Checking membership:
print("Is apple in the list?", "apple" in fruits)

# Looping through a list:
for fruit in fruits:
    print("Fruit:", fruit)

# List length:
print("Number of fruits:", len(fruits))
