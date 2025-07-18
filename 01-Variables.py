# =========================
#     PYTHON VARIABLES
# =========================

# In Python, a variable is like a label we stick on a value.
# We use the equals sign (=) to assign a value to a variable.

# Let's explore the main types of data we can store in variables!

# -------------------------------------
# 1. STRING (str): Textual data
name = "Adam"  # A person's name is usually a string

# -------------------------------------
# 2. NUMERIC TYPES
age = 30              # int: whole number
height = 1.75         # float: decimal number
complex_num = 2 + 3j  # complex: used in advanced math (you won’t need this often)

# -------------------------------------
# 3. BOOLEAN (bool): True or False values
is_student = True
has_graduated = False

# -------------------------------------
# 4. SEQUENCES

# - List: A changeable (mutable), ordered collection
fruits = ["apple", "banana", "cherry"]

# - Tuple: Like a list, but cannot be changed (immutable)
colors = ("red", "green", "blue")

# - Range: A sequence of numbers, often used in loops
even_numbers = range(0, 10, 2)  # 0, 2, 4, 6, 8

# -------------------------------------
# 5. MAPPING TYPE

# - Dictionary (dict): Stores data as key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
# You can access values by their key:
print(person["name"])  # Output: Alice

# -------------------------------------
# 6. SET TYPES

# - Set: An unordered collection of unique values
my_set = {1, 2, 3, 3}  # Python will automatically remove duplicates
print(my_set)  # Output: {1, 2, 3}

# - Frozenset exists too, but don’t worry about it for now :)

# -------------------------------------
# 7. NONE TYPE

# - None: Represents the absence of a value
mystery_value = None
print(mystery_value)  # Output: None

# -------------------------------------
# That’s a quick tour of the most common variable types in Python!
