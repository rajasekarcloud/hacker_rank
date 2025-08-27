class Team:
    def show_ID(self):
        print(self.get_ID())
    def get_ID(self):
        return "anonymous"
class A(Team):
    def get_ID(self):
        return "Alpha"

a = A()
a.show_ID()