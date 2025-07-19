# ============================
#        TYPE CASTING
# ============================

# Type casting is the act of converting data from one type to another

# --- String to Integer ---
str_num = "42"
int_num = int(str_num)
print(int_num + 10)  # Output: 52

# --- String to Float ---
str_float = "3.14"
float_num = float(str_float)
print(float_num + 1)  # Output: 4.14

# --- Number to String ---
age = 20
age_str = str(age)
print("I am " + age_str + " years old.")  # Output: I am 20 years old.

# --- Float to Integer ---
decimal = 9.99
whole = int(decimal)
print(whole)  # Output: 9

# --- Boolean to Integer ---
# True becomes 1, False becomes 0
print(int(True))   # Output: 1
print(int(False))  # Output: 0

# --- Input Example ---
# user_input = input("Enter a number: ")
# converted = int(user_input)
# print("You entered:", converted)

# If you try to cast something invalid, it will raise an error
# Example:
# int("hello")  # This will raise ValueError
