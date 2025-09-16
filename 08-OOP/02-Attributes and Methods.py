# ============================
#     ATTRIBUTES & METHODS
# ============================
# Attributes are variables inside a class
# Methods are functions inside a class

class Car:
    def __init__(self, brand, model):
        # "__init__" is a special method called a CONSTRUCTOR
        # It runs automatically when a new object is created
        self.brand = brand  # instance attribute
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving 🚗")

# Create objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model 3")

# Access attributes
print(car1.brand, car1.model)
print(car2.brand, car2.model)

# Call method
car1.drive()
car2.drive()
