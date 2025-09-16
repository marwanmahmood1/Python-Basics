# ==============================
#       RETURN STATEMENTS
# ==============================

#In a function call, arguments can be passed in two ways:
# 1. Positional Arguments, in which the order of the given parameters matters
# 2. Keyword Arguments, where the user can explicitly specify parameter names

# Example:
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Positional Arguments
greet("Alice", 25)

# Keyword Arguments (the order doesn't matter)
greet(age=30, name="Bob")

# Keyword arguments improve code readability and allow you to change the order of arguments safely:

def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

# Using default for age
greet("Charlie")

# Overriding with keyword
greet("David", age=40)

# When to Use:
#    - When functions have many parameters
#    - When you want clearer code
#    - When you need to skip optional parameters