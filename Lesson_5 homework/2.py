# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

import os

path = os.path.join('files', '2.txt')

file = open(path, "r", encoding='utf-8')
lines = file.readlines()
print(f'Количество строк: {len(lines)}')

count = 1
count2 = 0
for word in lines:
	print(f'Строка {count} - Количество слов: {len(word.split())}')
	count+=1
	for j in word:
		count2+=1
print(f'Количество символов: {count2}')
file.close()