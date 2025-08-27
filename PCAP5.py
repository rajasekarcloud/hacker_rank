x,y = (3.0, 0.0)
x,y = (0.0, 3.0)
try:
    z=x/y
except ArithmeticError:
    z = -1
else:
    z = -2
print(z)