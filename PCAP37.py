def boolean(op):
    return op(False, True)
print(boolean(lambda x,y: x if x else y))