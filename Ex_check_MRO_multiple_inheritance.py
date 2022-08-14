# Details can be refered to http://www.srikanthtechnologies.com/blog/python/mro.aspx

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 5


class D(B, C):
    pass

    #     A
    #    / \
    #   B   C
    #    \ /
    #     D

print(D.num) 
print(D.mro())


   