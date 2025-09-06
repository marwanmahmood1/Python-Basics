# =========================
#     IMPORTING MODULES
# =========================
# Python allows you to import external modules to use their functions and constants.

# Import the entire module
import math
print("Square root of 16:", math.sqrt(16))

# Import specific functions
from math import pi, factorial
print("Value of pi:", pi)
print("5! =", factorial(5))

# Import with an alias
import random as rnd
print("Random number between 1 and 10:", rnd.randint(1, 10))

# An example on importing custom modules:
# Suppose you created a file "my_module.py" with a function greet()
# You then type: 
#   from my_module import greet
#   greet("Alice")
