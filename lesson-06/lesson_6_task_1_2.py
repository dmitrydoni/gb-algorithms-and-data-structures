import random
import sys

# Task: In an array, find the maximal negative element. Print its value and position in the array.
# Version 2
n = 10
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
Variable: i, Memory: 50 bytes
Variable: idx, Memory: 52 bytes
Variable: max_neg_element, Memory: 64 bytes
Variable: all_v, Memory: 54 bytes
Total memory: 429
"""
