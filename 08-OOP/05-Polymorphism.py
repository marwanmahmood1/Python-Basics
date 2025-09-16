# =========================
#       POLYMORPHISM
# =========================
# Polymorphism = "many forms"
# Different classes can have methods with the same name but different behavior.

class Bird:
    def make_sound(self):
        print("Chirp")

class Dog:
    def make_sound(self):
        print("Woof")

class Cat:
    def make_sound(self):
        print("Meow")

# Function that works with any animal
def animal_sound(animal):
    animal.make_sound()

# Test
bird = Bird()
dog = Dog()
cat = Cat()

animal_sound(bird)
animal_sound(dog)
animal_sound(cat)
