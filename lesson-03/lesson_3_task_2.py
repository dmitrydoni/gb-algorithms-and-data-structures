"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
"""

import random

first = [random.randint(0, 100) for _ in range(10)]
second = []
print("Randomly generated array: ", first)

for n in first:
    if n % 2 == 0:
        idx = first.index(n)
        second += [idx]
print("Indexes of even numbers: ", second)
