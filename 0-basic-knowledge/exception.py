from pathlib import Path

try:
    print(5 / 0)
except ZeroDivisionError:
    print('You can not divide by zero')

try:
    print('我要操烂张语桐的骚逼')
except FileExistsError:
    path = Path.read_text('zyt.fuckyou')

