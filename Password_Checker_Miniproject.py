# =========================
# PASSWORD STRENGTH CHECKER
# =========================

import string  # for special characters set

# Common weak password samples
weak_passwords = ["11111111", "password", "12345678", "qwerty", "abc123"]

print("Welcome to the Password Strength Checker!")
password = input("Please enter your password: ")

# Weak password check
if password in weak_passwords:
    print("Your password is too common and easy to guess. Please choose a stronger password.")
else:
    strength_score = 0

    # Check minimum length
    if len(password) >= 8:
        strength_score += 1

    # Check for uppercase
    if any(char.isupper() for char in password):
        strength_score += 1

    # Check for lowercase
    if any(char.islower() for char in password):
        strength_score += 1

    # Check for digits
    if any(char.isdigit() for char in password):
        strength_score += 1

    # Check for special characters
    special_characters = string.punctuation
    if any(char in special_characters for char in password):
        strength_score += 1

    # Strength rating
    if strength_score <= 2:
        print("Password Strength: WEAK")
    elif strength_score == 3 or strength_score == 4:
        print("Password Strength: MEDIUM")
    else:
        print("Password Strength: STRONG")
