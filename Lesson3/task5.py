"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

total_sum = 0


# sum2 вернет True если в numbers встретилось Q и False, если не встретилось
def sum2(numbers):
    global total_sum
    for x in numbers.split(' '):
        if x.isnumeric():
            total_sum += int(x)
        elif x.upper() == 'Q':
            return True
        else:
            print(f'"{x}" -- не число!')
    return False


while True:
    a = input('Введите строку чисел, разделенных пробелом: ')
    must_exit = sum2(a)
    print(f'Сумма чисел: {total_sum}')
    if must_exit:
        break
