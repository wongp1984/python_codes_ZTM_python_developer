# Decorator
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1}s')
        return result
    return wrapper


@performance
def long_time1():
    for i in range(10000000):
        i*5


@performance
def long_time2():
    for i in list(range(10000000)):
        i*5


long_time1()
long_time2()
