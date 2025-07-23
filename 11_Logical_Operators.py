# ============================
#        LOGICAL OPERATORS
# ============================

# Logical Operators are those that build on conditionals and allow for more complex decision-making in programs
# What You Learned:
# - 'and' requires both conditions to be True
# - 'or' allows action if at least one condition is True
# - 'not' reverses the value of a boolean condition (True becomes False, and vice versa)

# - Comparison operators: age >= 18
# This script demonstrates how to use logical operators (and, or, not) in decision-making with simple real-world examples.

# Example: Club Entry Checker

age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").strip().lower() == "yes"
is_special_guest_day = input("Is it a special guest day? (yes/no): ").strip().lower() == "yes"

# Using logical operators to decide entry
can_enter = (age >= 18 and has_id) or is_special_guest_day

if can_enter:
    print("You may enter the club.")
else:
    print("Sorry, you cannot enter.")

# Example: 'not' operator

is_raining = input("Is it raining outside? (yes/no): ").strip().lower() == "yes"

if not is_raining:
    print("It's a nice day to go for a walk!")
else:
    print("Better take an umbrella.")
