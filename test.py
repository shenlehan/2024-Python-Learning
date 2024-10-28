import requests
import random

def func():
    for i in range(1, 200, 2):
        print(i)

def get_random():
    return random.randint(1, 100)



# if __name__ == '__main__':
    # func()
    i = get_random()
    print(i)
    print(__file__)
    print(__name__)
