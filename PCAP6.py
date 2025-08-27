def fun(x):
    assert x>=0
    return x**0.5
def mid_level(x):
    try:
        fun(x)
    except Error:
        raise

try:
    x = mid_level(-1)
except RuntimeError:
    x=-1
except:
    x=-2
print(x)