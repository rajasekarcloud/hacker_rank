def f(a,b):
    return a(b)
print(f(lambda x:x and True, 1>0))