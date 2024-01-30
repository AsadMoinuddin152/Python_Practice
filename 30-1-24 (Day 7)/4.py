while True:
    try:
        # Get user input for option selection
        choice = input("Select an option (1-5): ")

        if choice == "1":
            # Test ValueError by trying to convert a non-integer string to an integer
            int("abc")
        elif choice == "2":
            # Test TypeError by attempting to concatenate a string and an integer
            "5" + 5
        elif choice == "3":
            # Test ZeroDivisionError by dividing a number by zero
            10 / 0
        elif choice == "4":
            # Test FileNotFoundError by attempting to open a nonexistent file
            open("nonexistent_file.txt")
        elif choice == "5":
            # Test a generic Exception by raising a custom exception
            raise Exception("Custom exception")
        else:
            # Invalid choice handling
            print("Invalid choice. Please select an option from 1 to 5.")
            break

    except ValueError as ve:
        # Handle ValueError exception and print the code along with the error
        print(f"A ValueError occurred: {ve}")
    except TypeError as te:
        # Handle TypeError exception and print the code along with the error
        print(f"A TypeError occurred: {te}")
    except ZeroDivisionError as zde:
        # Handle ZeroDivisionError exception and print the code along with the error
        print(f"A ZeroDivisionError occurred: {zde}")
    except FileNotFoundError as fnfe:
        # Handle FileNotFoundError exception and print the code along with the error
        print(f"A FileNotFoundError occurred: {fnfe}")
    except Exception as e:
        # Handle other exceptions and print the code along with the specific error message
        print(f"An error occurred: {e}")
    else:
        # No exception occurred
        print("No exception occurred.")
    finally:
        # Execute code in the finally block regardless of whether an exception occurred or not
        print("This is the finally block.")
