#comprehension in list, dict, set

alist = [x for x in 'hello']
blist = {x for x in range(0, 100)}
clist = [x*2 for x in range(0, 10)]
dlist = {x**2 for x in range(0, 10) if x % 2 == 0}

print(alist)


simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(simple_dict.items())
my_dict = {key: val**2 for key, val in simple_dict.items() if val % 2 != 0}

print(my_dict)

my_dict2 = {num: num*2 for num in [1, 2, 3, 4, 5] if num % 2 != 0}
