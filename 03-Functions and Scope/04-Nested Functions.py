# ==========================
#      NESTED FUNCTIONS
# ==========================
# A nested function is simply a function defined INSIDE another function.
# Why use them?
# - To keep your code organized
# - To create "helper" functions that are only useful inside a bigger function
# - To demonstrate scope (inner functions can access variables from the outer one)

def outer_function():
    print("This is the outer function.")

    # Inner (nested) function
    def inner_function():
        print("This is the inner function. It only works inside outer_function.")

    # Call the inner function from within the outer function
    inner_function()

# Call the outer function
outer_function()

# inner_function() triggers an error saying: Can't call inner_function outside outer_function

# -------------------------------------

# Example 2: Nested functions can use variables from the outer function
def greet_person(name):
    def message():
        return f"Hello, {name}! Welcome aboard!"

    return message()  # inner function is CALLED and its result is returned

print(greet_person("Alice"))
print(greet_person("Bob"))

# -------------------------------------

# Example 3: Returning the inner function itself
def power_raiser(x):
    def raise_power(n):
        return n ** x  # inner function uses 'x' from the outer function
    return raise_power  # returning the function, not calling it yet

square = power_raiser(2)   # returns a function that squares numbers
cube = power_raiser(3)     # returns a function that cubes numbers

print(square(5))
print(cube(2))