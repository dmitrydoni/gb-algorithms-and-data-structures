"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

arr = [random.randint(-100, 100) for _ in range(20)]
print("Randomly generated array: ", arr)

arr_neg = []  # array of negative elements

for itm in arr:
    if itm < 0:
        arr_neg.append(itm)

max_neg_element = arr_neg[0]

for n in arr_neg:
    if n > max_neg_element:
        max_neg_element = n

print("Max negative element: ", max_neg_element)
