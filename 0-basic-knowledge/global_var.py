x = 1

def change_global():
    global x # declare that x is a global variable
    x += 1

print("x is now:%d" % (x))
change_global()
print("x is now:%d" % (x))

name = 100
def change_name(name):
    print("the result should be: %d" % (name + globals()["name"])) # to use the global variable

change_name(10)

