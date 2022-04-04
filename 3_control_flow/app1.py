# 1 comp operators
# ord - numeric represent
a = ord("b")
b = ord("B")
print(a == b)
print(a, b)

# 2 cond statements
print("\n2*********************")
temperature = 15
if temperature > 30:
    print("its warm")
elif temperature > 20:
    print("its nice")
else:
    print("its cold")
print("done")


# 3 ternary operater
print("\n3*********************")
age = 22
# if age >= 18:
#    message = "eligible"
# else:
#    message = "not eligible"   OR
# THIS IS ternary operator
message = "eligible" if age >= 18 else "not eligible"
print(message)

# 4 logical operator
# or and not
print("\n4*********************")

high_income = True
good_credit = True
student = False
# имеет право если не студент и (выс.доход или хорошая история)
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")


# 5- Short-circuit Evaluation
print("\n5*********************")
# если первый оператор False - дальше не считает
# if high_income and good_credit and not student:

# or - при нахождении первого True - расчет остановится
# if high_income or good_credit or not student:

# 6- Chaining Comparison Operators
print("\n6 *********************")
# age between 18 and 65

age2 = 22
if age2 >= 18 and age2 < 65:
    # same code as below
    # if 18 <= age2 < 65:
    print("Eligible**")

#7- Quiz
print(ord("b"), ord("a"), ord("c"))
