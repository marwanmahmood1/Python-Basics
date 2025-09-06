# =========================
#          TUPLES
# =========================
# Tuples are like lists, but they are IMMUTABLE (cannot be changed after creation).
# Use them when you want to store a fixed collection of items.

# Creating a tuple
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Accessing elements (just like lists, using indexes)
print("X:", coordinates[0])
print("Y:", coordinates[1])

# Tuples can hold mixed data types
person = ("Alice", 25, "Engineer")
print("Person:", person)

# Looping through a tuple
for item in person:
    print(item)

# Tuple unpacking (extracting values directly)
name, age, job = person
print(f"Name: {name}, Age: {age}, Job: {job}")

# Tuples are immutable → this will cause an error:
# person[1] = 30
