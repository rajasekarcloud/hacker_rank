vect=["alpha", "bravo", "charlie"]
new_vect = filter(lambda s: s[-1].upper() in ["A", "O"], vect)
for x in new_vect:
    print(x[1],end=" ")