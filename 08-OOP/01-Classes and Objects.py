# =========================
#     CLASSES & OBJECTS
# =========================
# A class is like a blueprint/template for creating objects.
# An object is an instance of a class, built from the blueprint.

# Example 1: A simple class
class Dog:
    # A method inside a class always takes "self" as the first argument
    def bark(self):
        print("Woof!")

# Creating objects (instances of the Dog class so we can use its methods/attributes)
dog1 = Dog()
dog2 = Dog()

# Calling a method (telling each object to perform the action defined in the class)
dog1.bark()
dog2.bark()

