"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    if a >= b >= c or b >= a >= c:
        return a + b
    if a >= c >= b or c >= a >= b:
        return a + c
    if c >= b >= a or b >= c >= a:
        return b + c
    return a + a


print('pass' if my_func(1, 1, 1) == 2 else 'fail')
print('pass' if my_func(1, 2, 3) == 5 else 'fail')
print('pass' if my_func(1, 3, 2) == 5 else 'fail')
print('pass' if my_func(3, 2, 1) == 5 else 'fail')
print('pass' if my_func(2, 1, 2) == 4 else 'fail')
print('pass' if my_func(2, 1, 1) == 3 else 'fail')
print('pass' if my_func(-1, 0, 1) == 1 else 'fail')
print('pass' if my_func(-2, -1, 0) == -1 else 'fail')
print('pass' if my_func(0, 2, 10) == 12 else 'fail')
