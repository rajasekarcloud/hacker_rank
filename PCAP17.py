from pylint.checkers.utils import has_starred_node_recursive


class Ceil:
    Token=1
    def get_token(self):
        return 1
class Floor(Ceil):
    def get_token(self):
        return 2
    def set_token(self):
        pass
holder = Floor()
print(hasattr(holder,"Token"))
print(hasattr(Ceil,"set_token"))