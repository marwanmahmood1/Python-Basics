# =========================
#     CUSTOM EXCEPTIONS
# =========================
# You can create your own exception classes by extending Exception.

class NegativeAgeError(Exception):
    """Raised when age is negative"""
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")
    print(f"Age is set to {age}")

try:
    set_age(-5)
except NegativeAgeError as e:
    print("Custom Error:", e)
