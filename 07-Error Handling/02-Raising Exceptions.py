# =========================
#     RAISING EXCEPTIONS
# =========================
# Sometimes you want to manually raise an error.
# This is where we use the `raise` keyword to trigger an exception.

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds!")
    return balance - amount

try:
    print(withdraw(100, 150))
except ValueError as e:
    print("Error:", e)
