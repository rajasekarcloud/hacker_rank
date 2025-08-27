import random
random.seed(0)
x=random.choice([1,2])
# random.seed(0) sets the seed for Python's random number generator to a fixed value (0 in this case),
# making the results deterministic and repeatable.
random.seed(0)
y=random.choice([1,2])
print(x-y)