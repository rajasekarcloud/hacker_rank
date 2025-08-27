class Failure(IndexError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "problem"
try:
    print("launch")
    raise Failure("ignition")
except RuntimeError as error:
    print(error)
except IndexError as error:
    print("ignore")
else:
    print("landing")