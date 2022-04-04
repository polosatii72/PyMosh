# 14- Exercise
print("\n14- Exercise**************")
# напечатать четные числа от 1 - 10
# напечатать кол-во четных
even_count = 0
for x in range(1, 10):
    if x % 2 == 0:
        even_count += 1
        print(x)
print(f"We have {even_count} even numbers")
