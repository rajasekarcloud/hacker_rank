class Package:
    spam=''
    def __init__(self,content):
        Package.spam += content + ';'
envelope_1=Package('Capacitor')
envelope_2=Package('Transistor')
print(envelope_2.spam)