# map, filter, zip and reduce
from functools import reduce


def multiple_by2(item):
    return item*2


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print('How map works:')
print(list(map(multiple_by2, [2, 4, 6])))
print('')

print('How filter works:')
print(list(filter(check_odd, [2, 7, 6, 9])))
print('')

alist = [1, 2, 3]
blist = [4, 5, 6, 7, 8, 9]

print('How zip works:')
print(list(zip(alist, blist)))
print('')

print('How reduce works:')
print(reduce(accumulator, blist, 5))
print('')
