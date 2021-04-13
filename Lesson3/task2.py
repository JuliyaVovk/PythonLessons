"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(name='', last_name='', city='', year_ob=0, mail='', phone=''):
    data = []
    if name:
        data.append(f'Имя: {name}')
    if last_name:
        data.append(f'Фамилия: {last_name}')
    if year_ob:
        data.append(f'Год рождения: {year_ob}')
    if city:
        data.append(f'Город проживания: {city}')
    if mail:
        data.append(f'E-mail: {mail}')
    if phone:
        data.append(f'Телефон: {phone}')
    print(', '.join(data))


user_data(
    city='Брайтон',
    name='Юля',
    last_name='',
    year_ob=0,
    mail='example@example.com',
    phone='(000) 111-22-33'
)
