a = [1, 2, 3, 4, 5]
b = a
print(b is a)
print(b == a)
print()

b[1] = 3
print(a)
print(b)
print()

c = (1, 2, 3, 4, 5)
d = c
print(c is d)
print(c == d)
print()

def func():
    x = (1, 2, 3, 4, 5)
    return x

e = func()
f = func()
print(e is f) # they are the same! use deepcopy to solve this!
print(e == f)
print()

def func1():
    g = [1, 3, 5, 7, 9]
    return g

h = func1()
i = func1()
print(h is i) # this is false
print(h == i)