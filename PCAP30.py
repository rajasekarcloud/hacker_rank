def inc(inc):
    def do(val):
        return val + inc
    return do
action = inc(-1)
print(action(2))
