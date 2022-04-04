#1- Lists

from audioop import reverse


letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
# * repear items in list
# + concats
zeros = [0] * 5
combined = zeros + letters
print(zeros)
print(combined)

numbers = list(range(20))
print(numbers)

# string to list items
chars = list("Hello world!")
print(chars)
print(len(chars))


# 2- Accessing Items
print("/n************")
letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0])  # 1st
print(letters[-1])  # end
print(letters[0:3])  # new list
print(letters[:3])  # same
print(letters[:])  # copy of original list
# 2 - step 0 and 3rd indexes    return every 2nd/3rd etc. element
print(letters[::2])

numbers = list(range(20))
print(numbers[::2])  # print even numbers
print(numbers[::-1])  # reverse order

# 3- List Unpacking
print("/n************")
numbers1 = [1, 2, 3]
first, second, third = numbers1

# ex. unpacking & packing
print("\nex. unpacking & packing")
# если значений много
# первые 2 значения - остальное в список
numbers2 = [1, 2, 3, 4, 4, 4, 4, 4, 4]
first, second, *other = numbers2
print(first)
print(second)
print(other)

# если нужен первый и последний эл-мент
numbers3 = [1, 2, 3, 4, 4, 4, 4, 4, 9]
first, *other, last = numbers3
print(first, last)
print(other)

# 4- Looping over Lists
print("/n************")
letters = ["a", "b", "c"]
# func enumerate wich is iterable
# на каждой итерации вернет кортеж (0, 'a') - индекс и айтем
# кортеж рид онли - не добавить элементов

# unpacking
#items = [0, "a"]
#index, letter = items

# enumerate - если нужен индекс
for index, letter in enumerate(letters):
    # 0 - индексы, 1 - значения
    print(index, letter)

# 5- Adding or Removing Items
print("/n************")
letters = ["a", "b", "c"]

# Add
# at the end append
letters.append("d")
# at beginnig
letters.insert(0, "---")
print(letters)
# remove last element or .pop(0) - указать с какого индекса
letters.pop()
print(letters)

# удалить первое встречное значение
letters.remove("b")
print(letters)

# удалить через функ del - элемент или диапазон
del letters[0:2]
print(letters)

# если надо очистить список
letters.clear()


# 6- Finding Items
print("/n************")
letters = ["a", "b", "c"]
print(letters.index("a"))

# print(letters.index("d")) # run time error
# check
if "d" in letters:
    print(letters.index("d"))

letters.append("d")
# найти кол-во встречающихся символов
print(letters)
print(letters.count("d"))


# 7- Sorting Lists
print("/n************  7- Sorting Lists")
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print("\n**")
# using sored func - any itarables
numbers1 = [4, 51, 2, 8, 6]
print(sorted(numbers1))  # return new list sorted
print(sorted(numbers1, reverse=True))  # return new list rev
print(numbers1)

print("\n**")
# list of order items
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# try sort this list
items.sort()
print(items)
# nothing changed - cos py IDK how sort this list

# принимает айтем и значение по которому будет сортировать
# сортируем по прайсу, цифрам


def sort_items(items):
    return items[1]  # 10,9,12


# в ключ передаем функцию по которой сортировка идет
# sort_items передаем ссылку на функцию, не вызывая ее как sort_items()
# во время сорт. каждый айтем попадает в функицю
print("\n**Sorted by price")
items.sort(key=sort_items)
print(items)
