"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке
и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""


def numbers_actions(num1, num2, action):
    if action == '+':
        print(num1 + num2)
    elif action == '-':
        print(num1 - num2)
    elif action == '*':
        print(num1 * num2)
    elif action == '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(num1 / num2)
    else:
        print("Invalid input.")


print("Please enter two numbers (Number 1, Number 2) and an action (+, -, *, / or 0 to exit).")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

while True:
    action = input("Action: ")
    if action != '0':
        print(numbers_actions(num1, num2, action))
    else:
        break
