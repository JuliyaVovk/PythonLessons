"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
"""


def divide(a, b):
    if b == 0:
        print('На ноль делить нельзя!')
        return None
    return a / b


n1 = float(input('Введите делимое: '))
n2 = float(input('Введите делитель: '))

result = divide(n1, n2)

print('Результат: ', result)


