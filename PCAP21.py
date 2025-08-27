class Economy:
    def __init__(self):
        self.econ_attr = True

class Business(Economy):
    def __init__(self):
        super().__init__()
        self.busn_attr = False
econ_a = Economy()
econ_b = Economy()
busn_a = Business()
busn_b = busn_a
print(isinstance(busn_a, Economy) and isinstance(econ_a, Business), end=" ")
print(busn_b is busn_a or econ_a is econ_b)