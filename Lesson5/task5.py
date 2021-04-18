"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint
from functools import reduce

file_name = 'data.txt'
n = 10
with open(file_name, 'w') as f:
    numbers = []
    for _ in range(n):
        numbers.append(str(randint(0, 100)))
    f.write(' '.join(numbers))

with open(file_name, 'r') as f:
    print(reduce(lambda a, b: a + b, map(lambda a: int(a), f.read().split(' '))))
