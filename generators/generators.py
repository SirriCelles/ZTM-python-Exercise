from time import time


def generator_function(num):
    for i in range(num):
        yield i * 2


g = generator_function(100)
next(g)
next(g)
print(next(g))


# using generators
def perfomance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'it took {t2 - t1} s')
        return result

    return wrapper


@perfomance
def long_time():
    print('1')
    for i in range(10000000):
        i * 5


@perfomance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i * 5

long_time()
long_time2()