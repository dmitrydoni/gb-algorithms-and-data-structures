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


# Version 3
def func_max_neg_element(n):
    # arr = [-36, -44, 5, 42, 77, -85, 40, -87, 75, 17, 0, 96, 42, -1, 1, 77, -39, 42, 1, 36]
    arr = [random.randint(-100, 100) for _ in range(n)]

    max_neg_element = float('-inf')
    idx = -1
    for i, itm in enumerate(arr):
        if 0 > itm > max_neg_element:
            max_neg_element = itm
            idx = i

    return max_neg_element


# test_func_max_neg_element(func_max_neg_element)

# cProfile.run('func_max_neg_element(20)')
# 115 function calls in 0.000 seconds

# cProfile.run('func_max_neg_element(100)')
# 539 function calls in 0.000 seconds

# cProfile.run('func_max_neg_element(1000)')
# 5293 function calls in 0.002 seconds

# cProfile.run('func_max_neg_element(10000)')
# 52741 function calls in 0.025 seconds

# timeit
# python -m timeit -n 1000 -s "import lesson_4_task_1_3" "lesson_4_task_1_3.func_max_neg_element(20)"

# "lesson_4_task_1_3.func_max_neg_element(20)"
# 1000 loops, best of 3: 24 usec per loop
# "lesson_4_task_1_3.func_max_neg_element(50)"
# 1000 loops, best of 3: 57.2 usec per loop
# "lesson_4_task_1_3.func_max_neg_element(100)"
# 1000 loops, best of 3: 110 usec per loop
# "lesson_4_task_1_3.func_max_neg_element(1000)"
# 1000 loops, best of 3: 1.1 msec per loop
# "lesson_4_task_1_3.func_max_neg_element(10000)"
# 1000 loops, best of 3: 11 msec per loop

