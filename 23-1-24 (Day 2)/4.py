# Get input string from the user
string = input()

# Calculate the length of the input string
n_string = len(string)

# Initialize an empty string to store the result
l_string = ''

# Iterate through the characters of the input string
for i in range(0, n_string):
    # Append characters with even indices to the result string
    if i % 2 == 0:
        l_string += string[i]

# Print the resulting string containing characters with even indices
print(l_string)
