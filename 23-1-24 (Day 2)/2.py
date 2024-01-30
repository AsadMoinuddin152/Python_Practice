# Define a function to check if a number is non-prime
def checkNonPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return num
    return 0

# Get input number from the user
number = int(input())

# Initialize a variable to store the total
total = 0

# Iterate through each digit of the input number
while number > 0:
    temp = number % 10
    # Add the non-prime digit to the total using the checkNonPrime function
    total += checkNonPrime(temp)
    number = number // 10

# Print the total sum of non-prime digits
print(total)
