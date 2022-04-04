from cmath import isnan, nan
from lib2to3.pytree import convert
import math

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # int after division
print(10 % 3)
print(10 ** 3)


x = 10
x = x + 3  # same x += 3

print(round(2.9))
print(abs(2.9))

# math module - math function -> top import
print(math.ceil(2.2))
# play with module
print(math.fsum([.1, .2, .3, .4]))
print(isnan(x))
print(math.sqrt(4))

# convert

x = input("a: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# print(type(x))
# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy values
# ""    0   None
