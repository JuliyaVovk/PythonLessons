"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
digit = input('Введите число: ')
number = int(digit)+int(digit+digit)+int(digit+digit+digit)
print(number)