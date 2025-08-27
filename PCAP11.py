class A:
    pass


o1 = A()
o2 = o1
o3 = A()
print(o1 is o2, o1 is o3)
print(o1)
print(o2)
print(o3)