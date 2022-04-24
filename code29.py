'''
iterable- __iter__() or __getitem__()
iterator- __next__()
iteration- process of iterator
'''
j = 19
# for i  in range (j): #generators
# print(i)


def gen(n):
    for i in range(0, n):
        # generators (This will not show value but gives information about location of variable)
        yield i
    #print('hello')


g = gen(3)
print(g)
print(g.__next__())       # for i in range(3):
print(g.__next__())     #       print(i)
print(g.__next__())
# print(g.__next__())    #this will not run because g=3 so it runs from g=0 to g=2
h='harry'
ier=iter(h)
print(ier.__next__())   #for i in range(ier):
print(ier.__next__())      #   print(i)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
