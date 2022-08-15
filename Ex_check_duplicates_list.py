some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dup_list = list()
for x in some_list:
    if some_list.count(x) > 1:
        if x not in dup_list:
            dup_list.append(x)
print(dup_list)

# modified to use comprehension of the list
dup_list2 = list(set([ch for ch in some_list if some_list.count(ch) > 1]))
print(dup_list2)
