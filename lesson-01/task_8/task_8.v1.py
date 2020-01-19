'''
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
Вариант решения с учётом возможностей языка python
'''

print('Please enter three numbers: a, b, c.')
a = float(input('Enter number a: '))
b = float(input('Enter number b: '))
c = float(input('Enter number c: '))

if b < a < c or c < a < b:
    print(f'Middle number: {a}')
elif a < b < c or c < b < a:
    print(f'Middle number: {b}')
else:
    print(f'Middle number: {c}')
