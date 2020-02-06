"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""


from collections import namedtuple

Enterprise = namedtuple('Enterprise', 'name, q1, q2, q3, q4, y')
n = int(input("How many enterprises do you have? "))
e_list = []  # list of enterprises
y_all = 0  # yearly profit from all enterprises
y_mean = 0  # mean yearly profit

for i in range(n):
    print(f'Enterprise {i+1}')
    name = input("Enterprise name: ")
    q1 = float(input("Q1 profit, $: "))
    q2 = float(input("Q2 profit, $: "))
    q3 = float(input("Q3 profit, $: "))
    q4 = float(input("Q4 profit, $: "))
    y = q1 + q2 + q3 + q4
    y_all += y
    y_mean = y_all / (i + 1)
    E = Enterprise(name, q1, q2, q3, q4, y)
    e_list.append(E)

above_mean = {}
below_mean = {}

for j in range(n):
    if e_list[j].y >= y_mean:
        above_mean[e_list[j].name] = e_list[j].y
    else:
        below_mean[e_list[j].name] = e_list[j].y

print("*" * 50)
print(f'Summary:\nYearly profit from all enterprises: {y_all}\nYearly average profit: {y_mean}')

print("\nEnterprises with profits equal to or greater than average:")

for k, v in above_mean.items():
    print(k, v)

print("\nEnterprises with profits lower than average:")

for k, v in below_mean.items():
    print(k, v)

print("*" * 50)
