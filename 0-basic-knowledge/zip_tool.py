names = ['a', 'b', 'c', 'd'] # tuple is also ok
ages = [1, 2, 3, 4]

# zip function will merge to array as a tuple
zippped_list = list(zip(names, ages))
print(zippped_list)

for name, age in zip(names, ages):
    print(name, age)

