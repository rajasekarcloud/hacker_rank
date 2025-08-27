class RangeError(IndexError):

    __errors = 0

    def __init__(self, the_index):
        IndexError.__init__(self, "erroneous index: " + str(the_index))
        RangeError.__errors += 1

    def get_error_counter(self):
        return RangeError.__errors


class Collection:
    def get(self, index):
        if not (1 <= index <= 10):
            raise RangeError(index)
        return 42


stuff = Collection()
try:
    print(stuff.get(1))
    print(stuff.get(0))
except RangeError as error:
    print("failure")
    print(error)
    print(error.get_error_counter())

