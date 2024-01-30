# DECORATES WITH PARAMETERS

# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}

user2 = {
    'name': 'Sorna',
    'valid': False  # changing this will either run or not run the message_friends function.
}

# Define an @authenticated decorator with parameters
def authenticated(fn):
    def wrapper(*args, **kwargs):
        # Check if the user is valid
        if args[0]['valid']:
            print("Valid user")
            # Call the original function if the user is valid
            fn(*args, **kwargs)
        else:
            print('You are not a valid user')

    return wrapper

# Apply the @authenticated decorator to the message_friends function
@authenticated
def message_friends(user):
    print('Message has been sent')

# Call the decorated function with different user objects
message_friends(user1)
message_friends(user2)
