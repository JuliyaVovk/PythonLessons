"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
seconds = int(input('Введите время в секундах: '))
hours = seconds // 3600
seconds -= hours * 3600
minutes = seconds // 60
seconds -= minutes * 60
print(f'Time is: {hours:02d}:{minutes:02d}:{seconds:02d}')
