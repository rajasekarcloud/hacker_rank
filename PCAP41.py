pairs = [[2,1],[-2,-1]]
print(sorted(pairs)) # [[-2, -1], [0, 0], [2, 1]]
new_pairs = map(lambda p: sorted(p), pairs)
print(list(new_pairs)[0][0])
print(list(new_pairs))
print(1/0)