# =========================
#     PYTHON VARIABLES
# =========================

# A variable is a name that refers to a value stored in memory.
# Use the equals sign (=) to assign a value to a variable.

# -------------------------------------
# 1. STRING (str): Textual data
name = "Adam"

# 2. NUMERIC:
age = 30              # int
height = 1.75         # float
complex_num = 2 + 3j  # complex

# 3. BOOLEAN (bool): True or False values
is_student = True

# 4. SEQUENCES:
# - List: Mutable, ordered
fruits = ["apple", "banana", "cherry"]

# - Tuple: Immutable, ordered
colors = ("red", "green", "blue")

# - Range: Immutable sequence of numbers
even_numbers = range(0, 10, 2)

# Example:
character_name = "John"
character_age = "35"

if character_name == "John":
    print("There once was a man named " + character_name + ", ")
    print("he was " + character_age + " years old.")

character_name = "Luke"

print("He did not like the name " + character_name + ", ")
print("but he also did not like being " + character_age + ".")
