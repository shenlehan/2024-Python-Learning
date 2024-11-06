from pathlib import Path

class Calculator:
    def calc(self):
        self.muffled = True

        try:
            while True:
                ls = input().split()
                print("%.5f" % (int(ls[0]) / int(ls[1])))
        except ZeroDivisionError:
            if self.muffled:
                print('You can not divide by zero')
            else: raise

c = Calculator()
c.calc()


# try:
#     raise Exception('This is an error message!')
# except Exception as e:
#     print(e)
#     raise ValueError from None

class SomeException(Exception): pass

try:
    raise SomeException('This is a self-defined message!')
except Exception as e:
    raise ValueError from Exception