# 8- For Loops
# repettion 3 times
# вывод строки / нумерация с 1 / добавление увелич кол-ва точек
print("8- For Loops***************")
for number in range(3):
    print("attempt", number + 1, (number + 1) * ".")

print("\n***************")

# с 1 до 10 не включая с шагом 2
for number in range(1, 10, 2):
    print("attempt", number, number * ".")

# 9- For..Else
print("\n9- For..Else***************")

# после первого входа в цикл выполнится условие с выходом из цикла
successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
print("end loop")

# выполняется весь проход цикла, т.к нет перехода к прерыванию
# если successful = True и будет break то else не будет выполнен!!!
print("\n***************")
successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("attempted 3 times and failed")


# 10- Nested Loops
print("\n10- Nested Loops ***************")
#
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

# 11- Iterables  / complex types such str,range, list and more
print("\n11- Iterables***************")

# print(type(5))
print(type(range(5)))  # return obj of type range # complex types
# iterable - example
# for x in range(5):   - итерация по каждому значению в ренже
# итерация по каждому символу
for x in "Pyt":
    print(x)

print("...")
for x in [1, 2, 3, 4]:
    print(x)


# 12- While Loops
# повторяем пока условие истино
print("\n12- While Loops***************")
# цикл половинного деления без остатка
number = 100
while number > 0:
    print(number)
    number //= 2

# консоль будет вводить > пока не ввести quit
# предусмотреть регистр - все перевести в нижний регистр
# сначала ввод будет переведен в нижний регистр и затем сравнит значения
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)


# 13- Infinite Loops
print("\n13- Infinite Loops**************")
# сразу сделали бесконечный цикл, не задав значения command
# по ходу дела будет проверять - предусмотреть выход!

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() != "quit":
        break
