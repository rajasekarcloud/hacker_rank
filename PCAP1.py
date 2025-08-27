import math
x=-1.5
# floor is more negative
# ceil is more positive
print(math.floor(x)) # Round to the nearest increment Eg: -1.5 -> -2
print(math.ceil(x)) # Round the nearset decrement Eg: -1.5 -> -1
print(abs(math.floor(x))) # Round to the nearest + Eg: -1.5 -> 2 and abs make positive -> 2
print(abs(math.floor(x) + (math.ceil(x)))) # 3

