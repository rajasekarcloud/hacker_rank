def f(l):
    return l(-3,3)
print(f(lambda x,y: x if x>y else y))