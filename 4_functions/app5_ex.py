# fizz-buzz algoritm  - interview question
# rules
# если ввод делится на 3 то вернет строку fizz
# если ввод делится на 5 то вернет строку buzz
# если ввод делится на 5 и 3 то вернет строку fizz-buzz

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return("fizz-buzz")
    elif input % 3 == 0:
        return("fizz")
    elif input % 5 == 0:
        return("buzz")
    else:
        return(input)


print(fizz_buzz(3))  # вернет строку fizz
print(fizz_buzz(5))  # вернет строку buzz
print(fizz_buzz(15))  # вернет строку fizz-buzz
print(fizz_buzz(7))  # вернет сам ввод 7  примеру как тут


# solve code - Mosh
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizz-buzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return("buzz")
    return input
