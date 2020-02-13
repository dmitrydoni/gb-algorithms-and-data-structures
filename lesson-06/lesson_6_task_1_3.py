import random
import sys

# Task: In an array, find the maximal negative element. Print its value and position in the array.
# Version 3
n = 10
arr = [random.randint(-100, 100) for _ in range(n)]
max_neg_element = float('-inf')
idx = -1

for i, itm in enumerate(arr):
    if 0 > itm > max_neg_element:
        max_neg_element = itm
        idx = i

print(max_neg_element)

# Memory allocation by variables
all_v = 0
for v in list(vars().keys()):
    if not v.startswith('_'):
        print(f'Variable: {v}, Memory: {sys.getsizeof(v)} bytes')
        all_v += sys.getsizeof(v)
print(f'Total memory: {all_v}')

"""
Variable: random, Memory: 55 bytes
Variable: sys, Memory: 52 bytes
Variable: n, Memory: 50 bytes
Variable: arr, Memory: 52 bytes
Variable: max_neg_element, Memory: 64 bytes
Variable: idx, Memory: 52 bytes
Variable: i, Memory: 50 bytes
Variable: itm, Memory: 52 bytes
Variable: all_v, Memory: 54 bytes
Total memory: 481
"""
