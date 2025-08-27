class Aircraft:
    def start(self):
        return "default"
    def take_off(self):
        start()
class Fixed_Wing(Aircraft):
    pass
class Rotor_Craft(Aircraft):
    def start(self):
        return "spin"
fleet = [Fixed_Wing(),Rotor_Craft()]
for airship in fleet:
    print(airship.start(), end=" ")