class SuperList(list):
    # def __init__(self):
    #     list.__init__(self)

    def __len__(self):
        return 88


super_list1 = SuperList()
super_list1.append('Hello1')
super_list1.append('Hello2')
super_list1.append('Hello3')

print(super_list1[0])
print(super_list1[2])
print(len(super_list1))

print(issubclass(SuperList, list))