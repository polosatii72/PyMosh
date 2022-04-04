# 3- Types of Functions

# 1. ex perform a task - выполняют действие

from tkinter import Y


def greet2(name):
    print(f"Hi {name}")


# 2. ex return a value - возвращают значение
round(1.9)

# пример 2го типа функции с возвратом значения


def get_greeting(name):
    return f"Hi {name}"


# получили значение функции с которым можно работать
message = get_greeting("Mosh")
# записали в файл значение
file = open("content.txt", "w")
file.write(message)


# 4- Keyword Arguments
def increment(number, by):
    return number + by


# если значение нужно разово - можно вывести сразу
print(increment(2, 1))
# Keyword Arguments - доб ключевое слово для понимания смысла
print(increment(2, by=1))


# 5- Default Arguments
# по умолчанию 1, и передавать не обязательно 2 значения в вызов
# либо передать другое свое значение
def increment(number, by=1):
    return number + by


print(increment(4))


#6- xargs
# *numbers - коллекция аргуметов, прим. передать 2,3,4,5 несколько
# для умножения
print("/n*************")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

#7- xxargs
print("/n*************")


def save_user(**user):
    print(user)
    print(user["id"])  # access to value


# key-value pairs
# object -dictionary    {'id': 1, 'name': 'John', 'age': 22}
# передав такую связку- пайтон создаст словарь
save_user(id=1, name="John", age=22)


#8- Scope
print("/n*************")

# name in greet and send_message differet, like messages

#global variable
message = "c"


def greet(name):
    global message   # !!!!! bad practice !!!
    message = "a"  # local variable


def send_message(name):
    message = "b"  # local variable


greet("Mosh")
print(message)
