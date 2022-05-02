n=int(input())

for i in range(1,n+1):
    k=i*i
    g=(i)*(i)-1
    l=(k*g)//2
    j=4*(i-1)*(i-2)
    print(l-j)
    
    ## this problem is about how many ways are there to place two kinghts on a chess board of i*i size where i=1,2,......n; so that they do not attack each other.
    
