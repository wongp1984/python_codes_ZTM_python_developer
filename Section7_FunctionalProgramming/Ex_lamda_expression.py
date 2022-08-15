# Square the list using lambda
my_list = [5, 4, 3]
print(list(map(lambda x: x**2, my_list)))

# List Sorting
a = [(9, 9), (0, 2), (10, -1), (4, 3)]
a.sort(key=lambda x: x[1])
print(a)
