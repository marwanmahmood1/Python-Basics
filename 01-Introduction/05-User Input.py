# =========================
#      USER INPUT
# =========================

# In Python, you can get input from the user using the input() function.

# Example: Ask the user for their name and greet them
name = input("What's your name? ")
print("Hello, " + name + "!")

# input() always returns a string, even if the user types a number.
# You need to convert it to another type if needed.

# Example: Ask for age and convert to integer
age = input("How old are you? ")
age = int(age)  # Now age is an integer
print("You will be " + str(age + 1) + " next year!")

# You can also convert to float if needed:
height = float(input("Enter your height in meters: "))
print("You are", height, "meters tall.")
