# =========================
# PASSWORD STRENGTH CHECKER
# =========================
# This script evaluates the strength of a given password based on:
# - Length
# - Uppercase & lowercase letters
# - Numbers
# - Special characters
# It also checks against a small list of common weak passwords as well as provides suggestions for improvement.

import string  # For special characters

# Common weak passwords
weak_passwords = ["123456", "password", "12345678", "qwerty", "abc123"]

print("Welcome to the Password Strength Checker!")
password = input("Enter your password: ")

# Check for common weak passwords
if password in weak_passwords:
    print("Your password is too common and easy to guess. Please choose a stronger password.")
else:
    strength_score = 0
    feedback = []

    # Minimum length
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase letters
    if any(char.isupper() for char in password):
        strength_score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letters
    if any(char.islower() for char in password):
        strength_score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digits
    if any(char.isdigit() for char in password):
        strength_score += 1
    else:
        feedback.append("Include at least one number.")

    # Special characters
    if any(char in string.punctuation for char in password):
        strength_score += 1
    else:
        feedback.append("Include at least one special character (e.g., !@#$%).")

    # Strength result
    if strength_score <= 2:
        print("Password Strength: WEAK")
    elif strength_score == 3 or strength_score == 4:
        print("Password Strength: MEDIUM")
    else:
        print("Password Strength: STRONG")

    # Print feedback if any
    if feedback:
        print("\nSuggestions to improve your password:")
        for tip in feedback:
            print("-", tip)
