class Base1:
      def func1(self):
            print("this is Base1 class")
class Base2:
      def func2(self):
            print("this is Base2 class")

class Child(Base1 , Base2):
      def func3(self):
            print("this is Base3 class")

obj = Child()
obj.func1()
obj.func2()
obj.func3()