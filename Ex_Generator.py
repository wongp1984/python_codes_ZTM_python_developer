def generator_func(num):
    for i in range(num):
        yield i*2  # yield is the keyword in generator.  yield pauses the generator_func after each time next() is called


g = generator_func(100)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for item in generator_func(10):
    print(item)
