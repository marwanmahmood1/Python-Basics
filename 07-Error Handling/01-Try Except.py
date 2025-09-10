# =========================
#        TRY / EXCEPT
# =========================
# Errors (exceptions) can stop a program from running.
# To prevent crashes, we can "handle" them using try/except.

# Example 1: Division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Example 2: Invalid input
try:
    number = int("abc")  # This will cause ValueError
except ValueError:
    print("Invalid input! Please enter a number.")

