#diamond shape problem(only in python,C++)
class A:
    def met(self):
        print(f"good morning class A ")
class B(A):
    def met(self):
        print(f"good morning class B")
class C(A):
    def met(self):
        print(f"good morning class C")
class D(C,B):
    #def met(self):
        #print(f"good morning class D")
    pass
a=A()
b=B()
c=C()
d=D()
d.met()
