"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

nums = [i for i in range(2, 100)]
print(nums)

divided_by_two = 0
divided_by_three = 0
divided_by_four = 0
divided_by_five = 0
divided_by_six = 0
divided_by_seven = 0
divided_by_eight = 0
divided_by_nine = 0

for n in nums:
    if n % 2 == 0:
        divided_by_two += 1
    if n % 3 == 0:
        divided_by_three += 1
    if n % 4 == 0:
        divided_by_four += 1
    if n % 5 == 0:
        divided_by_five += 1
    if n % 6 == 0:
        divided_by_six += 1
    if n % 7 == 0:
        divided_by_seven += 1
    if n % 8 == 0:
        divided_by_eight += 1
    if n % 9 == 0:
        divided_by_nine += 1

print(f'{divided_by_two} numbers are divided by 2')
print(f'{divided_by_three} numbers are divided by 3')
print(f'{divided_by_four} numbers are divided by 4')
print(f'{divided_by_five} numbers are divided by 5')
print(f'{divided_by_six} numbers are divided by 6')
print(f'{divided_by_seven} numbers are divided by 7')
print(f'{divided_by_eight} numbers are divided by 8')
print(f'{divided_by_nine} numbers are divided by 9')