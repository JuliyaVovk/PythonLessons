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


for t in [
    {'a': 1, 'b': 1, 'c': 1, 'expected': 2},
    {'a': 1, 'b': 2, 'c': 3, 'expected': 5},
    {'a': 1, 'b': 3, 'c': 2, 'expected': 5},
    {'a': 3, 'b': 2, 'c': 1, 'expected': 5},
    {'a': 2, 'b': 1, 'c': 2, 'expected': 4},
    {'a': 2, 'b': 1, 'c': 1, 'expected': 3},
    {'a': -1, 'b': 0, 'c': 1, 'expected': 1},
    {'a': -2, 'b': -1, 'c': 0, 'expected': -1},
    {'a': 0, 'b': 2, 'c': 10, 'expected': 12},
]:
    actual = my_func(t['a'], t['b'], t['c'])
    if t['expected'] == actual:
        print('Pass')
    else:
        print(f"Fail! Expected {t['expected']}, got {actual}")
