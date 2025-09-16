# ==============================
#       RETURN STATEMENTS
# ==============================

# A return statement sends a value back to the place where the function was called
# Without return, a function just runs its code and stops
# With return, you can store or use the result later

# How it's implemented:
# def function_name(parameters): <---- This sends it to do something
    # return value

# Simple Example:
def add_numbers(a, b):
    return a + b  # send back the result

# Use the returned value
result = add_numbers(5, 3)
print(result)  # Prints the output which is 8

# Checking if a number is Odd or Even:
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # Output: True
print(is_even(7))  # Output: False


# Example on multiple returns:
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error: Division by zero

