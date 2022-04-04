
#9- Debugging
from audioop import mul


print("/n*************")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


# дебаг - брейк пойнт - откуда пойдет дебаг
# F5 run deug,
# F10 - next, проход по строкам
# F11 - step into, зайти в функцию (в ней F10)
print("Start")
print(multiply(1, 2, 3))
