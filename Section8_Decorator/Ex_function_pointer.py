def hello():
    print('Hello!!!')


def greet(func):
    func()


sayhello = hello
del hello
sayhello()

greet(sayhello)
