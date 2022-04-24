# list comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i for i in a if i % 2 == 0]
print(a, b)
# set comprehension
alpha = {alpha for alpha in ["a", "a", "b", "c", "d", "d"]}
print(alpha)
# dict comprehension
Compdict = {i: f"Item {i}" for i in range(5)}
print(Compdict)
# genrator comprehension
gener = (i for i in range(5))
a = gener
print(a.__next__())
print(a.__next__())
print(a.__next__())
