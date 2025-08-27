def attic(x):
    assert x != 0
    return 1/x
try:
    x = attic(0)
except RuntimeError:
    x = -3
except:
    x = -2
else:
    x = -1
print(x)