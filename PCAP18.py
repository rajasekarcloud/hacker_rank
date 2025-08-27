class Top:
    def __str__(self):
        return '1'
class Left(Top):
    def __str__(self):
        return '2'
class Right(Top):
    def __str__(self):
        return '3'
class Bottom(Right,Left):
    pass

object = Bottom()
print(object)
print(Bottom.__mro__)