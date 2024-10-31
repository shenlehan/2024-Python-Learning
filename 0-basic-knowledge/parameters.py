def func1(names):
    for name in names:
        # print("hello, " + name)
        print(name)

def func2(*names): # python receives *names as a tuple
    print(names) 

def in_the_middle(x, *y, z):
    print(x, y, z)

def func3(**param): # python receives parameters as a dictionary
    print(param)

if __name__ == "__main__":
    s = ["a", "b", "c", "d", "e"]
    func1(s)
    func2('a', 'b', 'c', 'd', 'e')
    func2('f')
    in_the_middle('g', 'h', '233', z='asd')
    func3(x=1, y=2, z=3)