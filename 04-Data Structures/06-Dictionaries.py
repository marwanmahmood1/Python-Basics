# =========================
#       DICTIONARIES
# =========================
# Dictionaries store data in KEY:VALUE pairs, where:
# - Values can be of any type, but
# - Keys must be unique


# Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding / updating entries
student["grade"] = "A"
student["age"] = 22
print("Updated student:", student)

# Removing entries
del student["major"]
print("After deletion:", student)

# Looping through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
