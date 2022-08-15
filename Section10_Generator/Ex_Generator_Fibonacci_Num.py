# Generator implementation
print('** Generator implementation')


def fib_gen(num):
    FbLst = []
    for i in range(num+1):
        if (i == 0):
            FbLst.append(0)
            yield 0
        elif (i == 1):
            FbLst.append(1)
            yield 1
        else:
            # FbLst.append(FbLst[i-1] + FbLst[i-2])
            # yield FbLst[i]
            FbLst.append(FbLst[0] + FbLst[1])
            yield FbLst[2]
            FbLst.pop(0)


for n in fib_gen(5):
    print(n)


# List implementation
print('** List implementation')


def fib_lst(number):
    FbLst = []
    for i in range(number+1):
        if (i == 0):
            FbLst.append(0)
        elif (i == 1):
            FbLst.append(1)
        else:
            FbLst.append(FbLst[i-1] + FbLst[i-2])
    return FbLst


for n in fib_lst(5):
    print(n)
