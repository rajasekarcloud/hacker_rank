# Example

class A:
    pass
class B(A):
    pass


print(issubclass(A, B), issubclass(B, A), issubclass(B, B))

# Example

class A:
    pass


class B:
    pass


o = A()
print(isinstance(o, A), isinstance(o, B))

