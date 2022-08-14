#Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('Lucy', 2)
cat2 = Cat('Maya', 6)
cat3 = Cat('Bob', 4)


# 2 Create a function that finds the oldest cat
def GetOldesCat(lstcat):
    maxAge = -1
    maxCat = Cat('', 0)
    for x in range(len(lstcat)):
        if lstcat[x].age > maxAge:
            maxAge = lstcat[x].age
            maxCat = lstcat[x]

    return maxCat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldestCat = GetOldesCat([cat1, cat2, cat3])

print(f'The oldest cat is {oldestCat.age} years old')
