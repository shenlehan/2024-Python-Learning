def func(x):
    return x.isalnum() # len(x) >= 1 && x is comprised of alphabeta and numbers

seq = ["123z", "qwq", "dmyjqwdy", "*89**"]
print(list(filter(func, seq))) # the first parameter is a function for condition, the second one is the argument

print(list(map(str, range(10)))) # str() is a function to convert something into a string
# it's equal to:
print([str(i) for i in range(10)])

# lamda function
print(list(filter(lambda x: x.isalnum(), seq)))
# lamda x creates a simple anonymous function, and behind it is its body