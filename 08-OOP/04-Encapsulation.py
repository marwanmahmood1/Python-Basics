# =========================
#      ENCAPSULATION
# =========================
# Encapsulation is essentially restricting access to data (attributes/methods).
# In Python, this is done using naming conventions:
#   - public     (default) --> accessible everywhere
#   - _protected (with single underscore) --> meant for internal use
#   - __private  (with double underscore) --> name mangling, hard to access outside

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._balance = balance     # protected
        self.__pin = 1234           # private

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew {amount}. Remaining balance: {self._balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Access denied! Wrong PIN.")

# Test
account = BankAccount("Alice", 500)
account.deposit(200)
account.withdraw(100, 1234)
account.withdraw(100, 9999)  # Wrong PIN
