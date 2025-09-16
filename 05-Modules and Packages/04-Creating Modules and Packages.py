# =================================
#    CREATING MODULES & PACKAGES
# =================================

# --- Creating a Custom Module ---
# Step 1: Create a new Python file (e.g., my_module.py) in the same folder.
# Inside it, define some functions:
#
#   # my_module.py
#   def greet(name):
#       return f"Hello, {name}!"
#
#   def add(a, b):
#       return a + b
#
# Step 2: Import and use the module in another file:

import my_module

print(my_module.greet("Marwan"))   # Using custom greet function
print(my_module.add(5, 3))         # Using custom add function


# --- Creating a Package ---
# A package is a folder that contains an __init__.py file.
# Example structure:
#
# my_package/
# ├── __init__.py        (makes this folder a package)
# ├── math_utils.py      (module inside the package)
# └── string_utils.py    (another module)
#
# Contents of math_utils.py:
#   def multiply(a, b):
#       return a * b
#
# Contents of string_utils.py:
#   def shout(text):
#       return text.upper() + "!!!"
#
# Then you can import and use them like this:

# Import specific functions
from my_package.math_utils import multiply
from my_package.string_utils import shout

print(multiply(4, 6))   # Output: 24
print(shout("hello"))   # Output: HELLO!!!
