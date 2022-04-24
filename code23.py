# first of all python look for instance variable (overriding)
class A:
    var1 = "I am inside class A"

    def __init__(self):
        self.var1 = "this is instance variable in class A"   # this is a instance variable


class B(A):
    def __init__(self):  # mandatory(to use self we need to make a method/function)
        super().__init__()
        self.var1 = "I am inside class B" # this is a instance variable


a = A()
b = B()
print(b.var1)
print(a.var1)
print(b.var2)
