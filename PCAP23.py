class Alpha:
    def say(self):
        return "alpha"
class Beta(Alpha):
    def say(self):
        return "beta"
class Gamma(Alpha):
    def say(self):
        return "gamma"
class Delta(Beta, Gamma):
    pass

d = Delta()
b = Beta()
print(isinstance(d, Alpha))
print(d.say() == "gamma") # False
print(d.say())
print(Delta.__bases__)