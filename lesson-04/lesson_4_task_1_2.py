"""
Task: lesson_3_task_5
In an array, find the maximal negative element.
Print its value and position in the array.
Note: please do not confuse "minimal" and "maximal negative". These two are different values.
"""

import random
import cProfile


def test_func_max_neg_element(func):
    arr = [-36, -44, 5, 42, 77, -85, 40, -87, 75, 17, 0, 96, 42, -1, 1, 77, -39, 42, 1, 36]
    arr_neg = []  # array of negative elements

    for itm in arr:
        if itm < 0:
            arr_neg.append(itm)

    arr_max_neg = max(arr_neg)
    assert arr_max_neg == func()
    print('Test OK')


# Version 2
def func_max_neg_element(n):
    # arr = [-36, -44, 5, 42, 77, -85, 40, -87, 75, 17, 0, 96, 42, -1, 1, 77, -39, 42, 1, 36]
    arr = [random.randint(-100, 100) for _ in range(n)]

    i = 0
    idx = -1

    while i < n:
        if arr[i] < 0 and idx == -1:
            idx = i
        elif 0 > arr[i] > arr[idx]:
            idx = i

        i += 1

    max_neg_element = arr[idx]

    return max_neg_element


# test_func_max_neg_element(func_max_neg_element)

# cProfile.run('func_max_neg_element(20)')
# 111 function calls in 0.000 seconds

# cProfile.run('func_max_neg_element(100)')
# 527 function calls in 0.000 seconds

# cProfile.run('func_max_neg_element(1000)')
# 5241 function calls in 0.003 seconds

# cProfile.run('func_max_neg_element(10000)')
# 52746 function calls in 0.025 seconds

# timeit
# python -m timeit -n 1000 -s "import lesson_4_task_1_2" "lesson_4_task_1_2.func_max_neg_element(20)"

# "lesson_4_task_1_2.func_max_neg_element(20)"
# 1000 loops, best of 3: 25 usec per loop
# "lesson_4_task_1_2.func_max_neg_element(50)"
# 1000 loops, best of 3: 59.5 usec per loop
# "lesson_4_task_1_2.func_max_neg_element(100)"
# 1000 loops, best of 3: 118 usec per loop
# "lesson_4_task_1_2.func_max_neg_element(1000)"
# 1000 loops, best of 3: 1.18 msec per loop
# "lesson_4_task_1_2.func_max_neg_element(10000)"
# 1000 loops, best of 3: 11.6 msec per loop
