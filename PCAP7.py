class Accident(Exception):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return "problem"
try:
    print("action")
    raise Accident("accident")
except Accident as accident:
    print(accident)
else:
    print("success")