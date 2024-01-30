def divide(n1, n2):
    try:
        # Attempt to perform division and print the result
        print(n1 / n2)
    except ZeroDivisionError:
        # Handle division by zero error
        print("You can't divide by zero!")
    except ValueError:
        # Handle value error (non-numeric input)
        print("You must enter a number!")
    except:
        # Handle other exceptions
        print("Something went wrong!")
    # Return a success message regardless of the outcome
    return "Program is executed successfully"

# Get user input for two numbers and call the divide function
print(divide(int(input("Enter the first number: ")), int(input("Enter the second number: "))))
