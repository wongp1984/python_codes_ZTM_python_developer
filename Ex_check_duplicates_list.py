some_list = ['a','b','c','b','d','m','n','n']

dup_list = list()
for x in some_list:
    if some_list.count(x) > 1:
        if x not in dup_list:
            dup_list.append(x)
print(dup_list)