class RangeError(IndexError):
    pass

class Collection:
    def get(self, index):
        if not (1 <= index <= 10):
            raise RangeError
        return 42


stuff = Collection()
try:
    print(stuff.get(1))
    print(stuff.get(0))
except IndexError as error:
    print("failure")

