# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
import re
import os
path = os.path.join('files', '6.txt')

with open(path, "r", encoding='utf-8') as file:
	lines = file.readlines()
	dictionary = {}
	for line in lines:
		hours = sum(int(i) for i in re.findall(r'(\d+)\(\w+\)', line))
		subject = line.split()[0][:-1]
		dictionary[subject] = hours

print(dictionary)
