"""
Task: lesson_3_task_5
In an array, find the maximal negative element.
Print its value and position in the array.
Note: please do not confuse "minimal" and "maximal negative". These two are different values.
"""

import random


def test_func_max_neg_element(func):
    arr = [-36, -44, 5, 42, 77, -85, 40, -87, 75, 17, 0, 96, 42, -1, 1, 77, -39, 42, 1, 36]
    arr_neg = []  # array of negative elements

    for itm in arr:
        if itm < 0:
            arr_neg.append(itm)

    arr_max_neg = max(arr_neg)
    assert arr_max_neg == func()
    print('Test OK')


# Version 1
def func_max_neg_element(n):
    # arr = [-36, -44, 5, 42, 77, -85, 40, -87, 75, 17, 0, 96, 42, -1, 1, 77, -39, 42, 1, 36]
    arr = [random.randint(-100, 100) for _ in range(n)]
    arr_neg = []  # array of negative elements

    for itm in arr:
        if itm < 0:
            arr_neg.append(itm)

    max_neg_element = arr_neg[0]

    for i in arr_neg:
        if i > max_neg_element:
            max_neg_element = i

    return max_neg_element


# test_func_max_neg_element(func_max_neg_element)


# timeit
# python -m timeit -n 1000 -s "import lesson_4_task_1_1" "lesson_4_task_1_1.func_max_neg_element(20)"

# "lesson_4_task_1_1.func_max_neg_element(20)"
# 1000 loops, best of 3: 24.5 usec per loop
# "lesson_4_task_1_1.func_max_neg_element(50)"
# 1000 loops, best of 3: 57.4 usec per loop
# "lesson_4_task_1_1.func_max_neg_element(100)"
# 1000 loops, best of 3: 113 usec per loop
# "lesson_4_task_1_1.func_max_neg_element(1000)"
# 1000 loops, best of 3: 1.12 msec per loop
# "lesson_4_task_1_1.func_max_neg_element(10000)"
# 1000 loops, best of 3: 11.4 msec per loop
