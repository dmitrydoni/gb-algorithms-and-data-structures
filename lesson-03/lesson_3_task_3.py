"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

arr = [random.randint(-100, 100) for _ in range(10)]
print("Randomly generated array: ", arr)

max_element = arr[0]
min_element = arr[0]
max_element_idx = 0
min_element_idx = 0

for n in arr:
    if n > max_element:
        max_element = n
        max_element_idx = arr.index(max_element)
for n in arr:
    if n < min_element:
        min_element = n
        min_element_idx = arr.index(min_element)

print(f'Max element: {max_element}, index: {max_element_idx}')
print(f'Min element: {min_element}, index: {min_element_idx}')

min_max_swap_arr = arr[:]
min_max_swap_arr[max_element_idx] = arr[min_element_idx]
min_max_swap_arr[min_element_idx] = arr[max_element_idx]

print("\nArray with swapped Min and Max elements: ", min_max_swap_arr)
