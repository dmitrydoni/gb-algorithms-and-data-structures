"""
Определить, какое число в массиве встречается чаще всего.
"""

arr_most_freq_num = [-36, -44, 5, 42, 77, -85, 40, -87, 75, 17, 0, 96, 42, -44, 1, 77, -39, 42, 1, 36]
print("Test array to find the most frequently occurring number: ", arr_most_freq_num)

most_freq_num = arr_most_freq_num[0]
most_freq_num_cnt = 0

for n in arr_most_freq_num:
    n_freq = arr_most_freq_num.count(n)

    if n_freq > most_freq_num_cnt:
        most_freq_num_cnt = n_freq
        most_freq_num = n

print(f'Most frequently occurring number: {most_freq_num} (occurs {most_freq_num_cnt} times)')
