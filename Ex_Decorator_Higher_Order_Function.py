# a function which accepts a func or return a func is a higher order function
def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func

# a decorator is a higher order function which has a wrapper, and inside a wrapper you can boost the calling of the passed in func parameter

# decorator patter
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('*******************')
        func(*args, **kwargs)
        print('===================')
    return wrapper


@my_decorator
def hello(str, emoji=':>'):
    print(str, emoji)


def bye(str, emoji=':>'):
    print(str, emoji)


hello('HELLO!!',  emoji=':{')  # the hello function is boosted by the decorator
my_decorator(bye)('BYE!!')  # same as using a decorator
