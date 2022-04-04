# 8- Lambda Functions
from ast import Expression
print("\n************  8- Lambda Functions")


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


# def sort_items(items):
#    return items[1]  # 10,9,12


# в ключ передаем функцию по которой сортировка идет
# sort_items передаем ссылку на функцию, не вызывая ее как sort_items()
# во время сорт. каждый айтем попадает в функицю
print("\n**Sorted by price")

# 8! lambda
# определяем лямбду -  анонимную функ.
# syntax: parameters: expression
# в лямбде переписываем функцию def sort_items
# используем один раз для вызова
items.sort(key=lambda items: items[1])
print(items)


# 9- Map Function
print("\n************  9- Map Function")
# + more using lambdas in prg
# каждый айтем - это кортеж их 2х айтемов
# к примеру нужны только прайсы - трансформировать в список цифр
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# transformed or mapped list to different list
# 1st method
#prices = []
# for item in items:
#    prices.append(item[1])
# print(prices)


# 2nd method - map
# map func - takes lambda func and apply on every item in iterable
# проходит по итер. items и вызываем функ item: item[1] для каждого эл-та
# return iterable map object - <map object at 0x0000018AB0D3ED30>
x = map(lambda item: item[1], items)
for item in x:
    print(item)


print("\n***convert map obj to list obj")
prices = list(map(lambda item: item[1], items))
print(prices)
