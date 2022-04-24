from abc import ABCMeta, abstractclassmethod


class Shape(metaclass=ABCMeta):
    @abstractclassmethod
    def printarea(self):
        pass


class rectangle(Shape):
    type = 'rectangle'
    sides = 4

    def __init__(self):
        self.length = 5
        self.breadth = 6

    def printarea(self):
        return self.length * self.breadth


rect1 = rectangle()
print(rect1.printarea())
#obj=shape() we cannot make object of abstract class
