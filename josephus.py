import sys 
sys.setrecursionlimit(2000)
n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
k=int(input())
def josh(l,s,i):
    if(i==k-1):
        return l[s]
    else:
        del l[s]
        ns=(s+1)%len(l)
        return josh(l,ns,i+1)
    
print(josh(l,1,0))

## google on this topic to know more.
