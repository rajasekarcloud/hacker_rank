def f(a,b):
    return b(b)
print(f(lambda x: x + 1, 0))