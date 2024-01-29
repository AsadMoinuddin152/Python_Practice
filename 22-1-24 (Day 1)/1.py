class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Cat object with 3 cats
oggy = Cat('oggy', 1.5)
olly = Cat('olly', 2)
pinky = Cat('pinku', 0.7)

# Find the oldest cat
def Max_age(*args):
    return max(args)


# Output and name of the cat
print(f"The oldest cat is {Max_age(oggy.age, olly.age, pinky.age)} years old.")