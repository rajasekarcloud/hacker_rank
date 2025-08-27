def power(a):
    def internal(x):
        print('x',x)
        print('a',a)
        return x**a
    return internal
cube = power(3)
print(cube(2))