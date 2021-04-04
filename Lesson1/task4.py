"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
number = input('Введите число: ')
biggest = number[0]  # предположить, что первое число максимальное
index = 1  # начинаем сравнение со второго числа
while index < len(number):
    if number[index] > biggest:
        biggest = number[index]
    index += 1
print(f'Max is {biggest}')
