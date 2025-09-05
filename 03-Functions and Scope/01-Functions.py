# =========================
#       FUNCTIONS
# =========================
# Functions are reusable blocks of code that perform a specific task.
# Instead of repeating the same code multiple times, we define it once as a function and call it whenever needed.

# 1. Basic function without parameters (inputs)
def greet():
    print("Hello there!")
    print("Welcome to the world of Python functions!")
greet() # Calling the function

# 2. Function with parameters
def greet_person(name):
    print(f"Hello, {name}! Nice to meet you.")
greet_person("Alice")
greet_person("Bob") # Call the function with two different arguments

# 3. Function with return value
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 7)
print("The sum is:", result)

# 4. Using a function in another function
def calculate_area(length, width):
    return length * width

def display_area(length, width):
    area = calculate_area(length, width)
    print(f"The area of a {length}x{width} rectangle is {area}")

display_area(5, 3)

# 5. Default parameters
def greet_with_default(name="Friend"):
    print(f"Hello, {name}!")

greet_with_default()   # Uses default value
greet_with_default("Sarah")  # Overrides default

# 6. Keyword arguments
def introduce(name, age, city):
    print(f"My name is {name}, I am {age} years old, and I live in {city}.")

introduce(age=22, city="Cairo", name="Omar")
