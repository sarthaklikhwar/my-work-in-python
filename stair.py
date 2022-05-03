n=int(input())

def staris(n):
    if (n<=1):
        return 1
    
    return staris(n-2)+staris(n-1)


print(staris(n))
