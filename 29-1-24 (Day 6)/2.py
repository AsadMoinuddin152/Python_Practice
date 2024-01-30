from time import time

# Define a decorator 'performance' to measure the execution time of a function
def performance(fn):
    def wrapper(*args, **kwargs):
        # Record the start time
        t1 = time()
        
        # Call the original function
        fn(*args, **kwargs)
        
        # Record the end time
        t2 = time()
        
        # Print the elapsed time
        print('It took {}s'.format(t2 - t1))
    
    return wrapper

# Apply the 'performance' decorator to the 'long_time' function
@performance
def long_time():
    # Perform a time-consuming operation
    for i in range(10000000):
        (i * 5) / 99

# Apply the 'performance' decorator to the 'long_time2' function
@performance
def long_time2():
    print('2')
    # Perform another time-consuming operation
    for i in list(range(10000000)):
        (i * 5) ** 2

# Call the decorated functions
long_time()
long_time2()
