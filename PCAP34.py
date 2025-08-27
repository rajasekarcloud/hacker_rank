consts = [3.141592, 2.718282]
try:
    print(consts.index(314e-2))
except Exception as exception:
    print(exception.args)
else:
    print("success")