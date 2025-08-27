l=[x for x in range(1,10,3) if x%2 == 0]
print(len(l))

foo = [x for x in range(4)]
print(foo)
spam = [ x for x in foo[1:-1]]
print(len(spam))