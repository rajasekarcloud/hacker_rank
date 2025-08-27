class Tin:
    label="soup"
    def __init__(self,prefix):
        self.name = prefix + " " + Tin.label
        print(self.name)
        print(Tin.label)
can1=Tin("Tomato")
can2=Tin("Chicken")
print(can1.label)
print(can2.label)
print(can1.label == can2.label)