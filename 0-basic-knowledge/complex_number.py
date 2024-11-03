"""
This version is wrong.
You can only import the whole module and then use the functions
or just import one function from the module and use only one function with the same name
"""

# from cmath import sqrt
# from math import sqrt

# x1 = math.sqrt(2)
# x2 = cmath.sqrt(-1)

# print(x1, x2)

from cmath import sqrt
# import cmath

print(sqrt(-1))
# print(cmath.sqrt(-1)) use this while importing the whole module
# if use from _module_ import *
# we can still use the function without giving module's name