# Define the Pets class
class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

# Define the Cat class
class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

# Define the Simon class that inherits from Cat
class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Define the Sally class that inherits from Cat
class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Define the Minnu class that inherits from Cat
class Minnu(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Create a list of all the cats
my_cats = [Sally('Sally', 7), Simon('Simon', 8), Minnu('Minnu', 10)]

# Instantiate the Pets class with all the cats using variable my_pets
my_pets = Pets(my_cats)

# Output all the cats walking using the my_pets instance
my_pets.walk()
