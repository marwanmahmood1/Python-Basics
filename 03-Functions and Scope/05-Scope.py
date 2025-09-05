# =========================
#           SCOPE
# =========================
# Scope = The region of the code where a variable is recognized and can be used.
#
# Python follows the "LEGB Rule" for variable lookup:
# L = Local (inside current function)
# E = Enclosing (in parent function if nested)
# G = Global (declared at top-level of the file)
# B = Built-in (Python’s reserved names like len, print, etc.)

# -------------------------------------

# GLOBAL SCOPE
x = 10  # This variable is GLOBAL, accessible anywhere in the file

def show_global():
    print("Global x:", x)  # Can access global variable
show_global()

# -------------------------------------

# LOCAL SCOPE
def local_example():
    y = 20  # LOCAL variable: only exists inside this function
    print("Local y:", y)

local_example()
# print(y) results in an error saying: y is not defined outside the function

# -------------------------------------

# ENCLOSING (NESTED) SCOPE
def outer():
    z = "outer variable"

    def inner():
        print("Inner sees:", z)  # inner function can access 'z' from outer
    inner()

outer()

# -------------------------------------

# MODIFYING GLOBAL VARIABLES
count = 0

def increase_count():
    global count  # Use 'global' to modify the global variable
    count += 1
    print("Count is now:", count)

increase_count()
increase_count()

# -------------------------------------

# BUILT-IN SCOPE
# Example: "len" is a built-in function in Python
print(len("Hello"))  # Python looks in Built-ins if not found in Local/Global
