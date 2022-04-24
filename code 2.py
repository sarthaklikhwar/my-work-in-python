def inc(num):
    try:
        return int(num)+1
    except:
        return ValueError("this is wrong input")
b=inc('aSFSDGFD2343') 
print(b)           