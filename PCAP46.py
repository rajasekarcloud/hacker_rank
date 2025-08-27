class Failure(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "out of order"
try:
    print("turn on")
    raise Failure("crash")
except Failure as problem:
    print(problem)
else:
    print("success")
