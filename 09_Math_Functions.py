# =========================
#     PYTHON MATH FUNCTIONS
# =========================

# Python has built-in math functions, and more advanced ones in the math module

# --- Built-in math functions ---

print(abs(-5))            # Absolute value of a number
print(pow(2, 3))          # 2 to the power 3 = 8
print(round(3.14159))     # Round to nearest integer → 3
print(round(3.14159, 2))  # Round to 2 decimal places → 3.14
print(max(10, 20, 5))     # Largest number → 20
print(min(10, 20, 5))     # Smallest number → 5

# --- Math module functions ---
import math                  # Math functions are not available by default, so we use this command for the functions to work

print(math.sqrt(16))         # Square root → 4.0
print(math.floor(3.7))       # Floor rounds DOWN to the nearest integer → 3
print(math.ceil(3.1))        # Ceil round UP to the nearest integer → 4
print(math.pi)               # Pi constant → 3.141592...


# --- Trigonometry examples ---
print(math.sin(math.radians(30)))  # sin(30°) → 0.5
print(math.cos(math.radians(60)))  # cos(60°) → 0.5
# We apply math.radians on trigonometric functions to get the results in radians


# --- Logarithms and exponential ---
print(math.log(100, 10))      # Log base 10 of 100 → 2.0
print(math.exp(1))                     # e^1 → 2.718...
