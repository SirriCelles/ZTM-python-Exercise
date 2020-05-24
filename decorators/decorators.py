from time import time


# Building a custom decorator to calculate the performance of a function

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f' It took {t2 - t1} s')
        return result

    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i * 5


long_time()


# decorator definition
def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('********')

    return wrap_func


@my_decorator
def hello():
    print('Hello')
