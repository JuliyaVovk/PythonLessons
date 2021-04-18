"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

my_list = [{}, {'average_profit': 0.0}]
with open('firms.txt', 'r') as f:
    line = f.readline()
    while line:
        company = line.strip().split(' ')
        company_name, income, expenses = company[0], float(company[2]), float(company[3])
        margin = income - expenses
        if margin >= 0:
            my_list[1]['average_profit'] = (my_list[1]['average_profit'] + margin) / 2
        my_list[0][company_name] = margin
        line = f.readline()
print(my_list)
with open('companies.json', 'w') as out:
    print(json.dumps(my_list, indent=' '*4), file=out)
