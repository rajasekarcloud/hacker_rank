class Top:
    value = 3
    def say(self):
        return self.value
class Middle(Top):
    value = 2
class Bottom(Middle):
    def say(self):
        return -self.value

short = Bottom()
tall = Top()
average = Middle()
print(isinstance(average,Bottom))
print(tall.say())
print(average.value)
print(short.value)