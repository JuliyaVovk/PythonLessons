"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('test.txt', 'r') as f:
    text = f.read()
    lines = text.split('\n')
    print('Number of lines:', len(lines))
    for line in lines:
        if line:
            words = line.split(' ')
            # print('Words:', words)
            print('Number of words:', len(words))
