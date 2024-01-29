from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print('It took {}s'.format(t2-t1))
    return wrapper

@performance
def long_time():
    for i in range(10000000):
        (i*5)/99

@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        (i*5)**2

long_time()
long_time2()