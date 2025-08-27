class Collection:
    stamps = 2
    def __init__(self,stuff):
        self.stuff = stuff
    def dispose(self):
        del self.stuff
binder = Collection(1)
binder.dispose()
print(Collection.__dict__)
print(binder.__dict__)
