# =========================
#        INHERITANCE
# =========================
# Inheritance allows a class to use code from another PARENT class.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating 🍴")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof! 🐶")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow! 🐱")

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.eat()   # inherited from Animal
dog.bark()  # specific to Dog

cat.eat()   # inherited from Animal
cat.meow()  # specific to Cat
