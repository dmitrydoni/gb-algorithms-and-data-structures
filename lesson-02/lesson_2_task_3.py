"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

num_reversed = 0
num = int(input("Please enter a number: "))

while num > 0:
    right_digit = num % 10
    num_reversed = num_reversed * 10 + right_digit
    num = num // 10

print(f'Reversed number: {num_reversed}')
