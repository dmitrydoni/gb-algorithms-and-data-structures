'''
По введенным пользователем координатам двух точек вывести уравнение прямой, которая проходит через эти точки.
'''

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

if x1 == x2:
    print(f'Incomplete line equation:\nx - {x1} = 0')
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print(f'Line equation:\ny = {k} * x + {b}')