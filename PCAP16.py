class Class:
    class_var = 1
    def __init__(self):
        self.instance_var=1

    def method(self):
        pass
object = Class()
print(Class.__dict__)
print(Class.__dict__.keys())
print(object.__dict__.keys())