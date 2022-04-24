from typing import List


class Library:
    def __init__(self, abook1, abook2, abook3, abook4):
        self.book1 = abook1
        self.book2 = abook2
        self.book3 = abook3
        self.book4 = abook4

    def displayallbooks(self):
        List = [self.book1, self.book2, self.book3, self.book4]
        
        print('the books  available are-', List, '\n')

    def request(self):
        if b == self.book1 or b == self.book2 or b == self.book3 or b == self.book4:
            print('the book you want is alloted to you. \n')
            
        if b == self.book1 or b == self.book2 or b == self.book3 or b == self.book4:
            List = [self.book1, self.book2, self.book3, self.book4]
            l = [item for item in List if item not in b]
            print('the books now available are-',l ,'\n')
        else:
            return'sorry, the book you wanted is not available \n'
        
            

    def Return(self):
        #ist=[]
        if c == self.book1 or c == self.book2 or c == self.book3 or c == self.book4:
            List.add(c)
            print("the book you havr returned is -",List,'\n')

        print('thanks for returning this book.Hope to see you soon. \n')
        
        
        
        


sarthak = Library('roorkee', 'delhi', 'mumbai', 'agra')
while(True):  # menu driven program
    print('--- Welcome to Student library---')
    print("press 1- list all books")
    print("press 2- request a book")
    print("press 3-add/ return a book")
    print("press 4-exit")
    print('\n')
    a = int(input("enter your choice--"))
    if a == 4:
        break
    if a == 1:
        print(sarthak.displayallbooks())
    if a == 2:
        b = input("enter the name of book you want--- \n")
        print(sarthak.request())

    if a == 3:
        c=input("enter the name of the book you want to return")
        print(sarthak.Return())

print("Thank you....")
print('come back soon')
