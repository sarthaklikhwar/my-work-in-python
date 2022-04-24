class Parent():
    def first(self):
        print(f'Parent function')
        
class Child(Parent):
    def second(self):
        print('Child function')

sarthak = Child()
sarthak.first()
sarthak.second()