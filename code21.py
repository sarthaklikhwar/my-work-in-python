class level1:
      def first(self):
            print ('code',end=' ')

class level2(level1): #inherit level1
      def second(self):
             print ('with',end=' ')

class level3(level2): #inherit level2
      def third(self):
            print ('harry',end=' ')

obj=level3()
obj.first()
obj.second()
obj.third()