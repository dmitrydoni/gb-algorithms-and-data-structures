"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

even = 0
odd = 0
num = int(input("Please enter a number: "))

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    num //= 10

print(f'Even digits: {even}\nOdd digits: {odd}')
