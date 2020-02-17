"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""

import random


def sort_bubble(arr):
    n = len(arr)

    for i in range(n):

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    size = 10
    arr = [random.randint(-100, 99) for _ in range(size)]
    random.shuffle(arr)
    print(f'Original array: {arr}')
    sort_bubble(arr)
    print(f'Sorted array: {arr}')
