y=int(input())
x=int(input())

if(x>y):
    if x%2!=0:
        print(x*x-y+1)
    else:
        x=x-1
        print(x*x+y)
else:
    if(y%2==0):
        print(y*y-x+1)
    else:
        y=y-1
        print(y*y+x)
        
   ## this is a code for spiral game where y is the row number and x is column number.
        
