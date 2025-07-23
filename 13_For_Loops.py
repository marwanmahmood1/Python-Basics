# ======================
#         FOR LOOPS
# ======================

# A "for loop" is used to repeat a block of code for each item in a sequence.
# Imagine you have a list of items, and you want to do something with each one.
# Instead of writing print() for every single item, you let the "for" loop do it automatically.

# Syntax:
#   for variable in sequence:
#        do something with "variable"

# Python will go through each item in the sequence and temporarily store it in "variable".
# Then it runs the code inside the loop for each item.

# Example 1: Iterating over a list
fruits = ["apples", "bananas", "cherries"]
for fruit in fruits:
    print(f"I like {fruit}")

# Example 2: Iterating over a string
for letter in "Python":
    print(letter)

# Example 3: Using range() 
for number in range(1, 6):  # This iterates all numbers in a given span (start, stop) or (start, stop, step)
    print("Number:", number)
