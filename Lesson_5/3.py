# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
# Выполнить подсчет средней величины дохода сотрудников.

import os

path = os.path.join('files', '3.txt')
file = open(path, "r", encoding='utf-8')
content = file.readlines()

names, salaries, low_salary = [],[],[]
sum = 0
for line in content:
	i = line.split()
	names.append(i[0])
	salaries.append(float(i[1]))
	if float(i[1]) < 20000:
		low_salary.append((i[0]))
	sum+=float(i[1])

print(f'ЗП ниже 20000: {" ".join(low_salary)}')
print(f'Средняя зп - {sum/len(content)}')
