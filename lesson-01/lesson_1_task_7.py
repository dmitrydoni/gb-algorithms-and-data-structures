'''
Определить, является ли год, который ввел пользователь, високосным или не високосным.
'''

year = int(input('Please enter year (only numbers): '))
if year >= 0:
    if year % 4 == 0:
        print('Entered year is leap')
    else:
        print('Entered year is not leap')
else:
    print('Input is invalid')
