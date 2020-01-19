'''
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
Вариант решения буз учёта возможностей языка python
'''

print('Please enter three numbers: a, b, c.')
a = float(input('Enter number a: '))
b = float(input('Enter number b: '))
c = float(input('Enter number c: '))

if a > b:
    if a < c:
        print(f'Middle number: {a}')
    elif b > c:
        print(f'Middle number: {b}')
    else:
        print(f'Middle number: {c}')
else:
    if a > c:
        print(f'Middle number: {a}')
    elif b > c:
        print(f'Middle number: {c}')
    else:
        print(f'Middle number: {b}')
