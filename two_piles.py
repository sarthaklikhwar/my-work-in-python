t=int(input())

for i in range(0,t):
    a,b=map(int,input().split())
    if((a+b)%3==0):
        print("YES")
    else:
        print("NO")
    ## In this problem we have to find out that is it possible to remove total of a and b coins such that in one single move either from  one set of coins  one coin will be remove and two coins from other.
