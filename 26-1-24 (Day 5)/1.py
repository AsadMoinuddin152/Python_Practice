from functools import reduce

# Task 1: Capitalize all pet names in the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

# Function to capitalize a string
def Capitalize(i):
    return i.upper()

# Apply the Capitalize function to each element in the list using map
capitalized_pets = list(map(Capitalize, my_pets))
print(capitalized_pets)

# Task 2: Zip two lists into a list of tuples, sorting the numbers from lowest to highest
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

# Create a list of tuples by zipping my_strings and sorted my_numbers
my_zip = list(zip(my_strings, sorted(my_numbers)))
print(my_zip)

# Task 3: Filter scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

# Function to filter scores over 50%
def remove_under_50(i):
    return i > 50

# Use filter to select scores over 50%
filtered_scores = list(filter(remove_under_50, scores))
print(filtered_scores)

# Task 4: Combine all numbers in two lists using reduce and calculate the total
# Function to accumulate the sum of two numbers
def accumulator(acc, item):
    return acc + item

# Use reduce to accumulate the sum of my_numbers and scores
total_sum = reduce(accumulator, (my_numbers + scores))
print(total_sum)
