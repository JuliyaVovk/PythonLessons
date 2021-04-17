"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

salaries = []

with open('employees.txt') as f:
    file = f.read()
    my_list = file.split('\n')
    for el in my_list:
        employee, salary = el.split(' ')
        salary = float(salary)
        salaries.append(salary)
        if salary < 20000:
            print(f'Underpaid employee: {employee}')

print(f'Average salary: {sum(salaries) / len(salaries)}')
