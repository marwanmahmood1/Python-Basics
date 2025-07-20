# ============================
#      STRING METHODS
# ============================

# A string is a sequence of characters, and Python provides built-in methods to work with them

text = "  Hello, Python World!  "

# ---------------------------
# Basic string methods

print(text.lower())       # This leads to the string being printed in lowercase
print(text.upper())       # This leads to the string being printed in uppercase
print(text.strip())       # Strip removes any leading or trailing characters such as spaces, tabs, or new lines
print(text.replace("Python", "Coding"))  # We can replace words inside a string using this method, without tampering with the main string
print(text.split(","))    # Splits the string into separate words, followed by a comma

# ---------------------------
# Checking content

print(text.startswith("  He"))     # Evaluating whether the text starts with specific characters
print(text.endswith("!  "))        # Evaluating whether the text starts with specific characters
print("Python" in text)            # Evaluating whether the text contains specific characters
print(text.isalpha())              # Evaluating whether the whole string contains only alphabetical characters
print("Hello".isalpha())           # Evaluating whether the specified text contains only alphabetical characters

# ---------------------------
# String length and indexing
# Index starts from 0, not 1, therefore we always begin counting from 0

print(len(text))         # Length of the string including spaces
print(text[2])           # Third character
print(text[-1])          # Last character

# ---------------------------
# Concatenation and formatting
# Concatenation is the act of joining two or more sequences (strings, lists, or tuples) to create a new, combined sequence.

first = "Python"
second = "Rocks"
print(first + " " + second + "!")  # "Python Rocks!"

name = "Adam"
age = 25
print(f"My name is {name} and I'm {age} years old.")

# The line above was performed using "f-string formatting", basically a concise and readable way to embed Python expressions inside string literals for formatting