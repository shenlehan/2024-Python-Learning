nested = [[1, 2], [3], [4, 5, 6]]

def flatten(nested): # create a simple generator
    for sublist in nested:
        for element in sublist:
            yield element


for num in flatten(nested):
    print(num)
    print('paused!')