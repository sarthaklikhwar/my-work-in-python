def dec1(func1):
    def asd():

        print('executing now')

        func1()
        print("executed now")
    return asd

@ dec1
def qwe():
    print("good night")

a=dec1(qwe())
print(a)
