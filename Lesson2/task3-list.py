"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

month = input('Введите номер месяца: ')
if not month.isnumeric():
    print('Это не число!')
else:
    month = int(month)
    winter, spring, summer, autumn = [1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]
    if month in winter:
        print('Зима')
    elif month in spring:
        print('Весна')
    elif month in summer:
        print('Лето')
    elif month in autumn:
        print('Осень')
    else:
        print('Нет такого месяца!')
