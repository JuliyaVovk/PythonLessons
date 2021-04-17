"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

replacements = {
    'Zero': 'Ноль',
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
}
out = open('counts2.txt', 'w')
with open('counts.txt', 'r') as f:
    text = f.read()
    lines = text.split('\n')
    for el in lines:
        if el:
            words = el.split(' ')
            out.write(replacements[words[0]]+' - '+words[-1] + '\n')
