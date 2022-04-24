try:
    a=int(input("enter a num"))
    c=1/a
    exit()
except Exception as e:
    print(e)
    exit()
finally:
    print("huray we were sucessful")        