# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджеры контекста.
import os

with open(os.path.join('files', '7.txt'), "r", encoding='utf-8') as file_read:
	lines = file_read.readlines()
	dictionary = {}
	average_profit = {}
	l = []
	sum = 0
	count = 0
	for line in lines:
		name = line.split()[0]
		form = line.split()[1]
		sales = float(line.split()[2])
		loss = float(line.split()[3])
		dictionary[name] = sales-loss
		if sales > loss:
			sum += sales-loss
			count += 1
		
average_profit['average_profit'] = sum/count
l.append([dictionary, average_profit])
print(l)

import json
with open(os.path.join('files', '7.json'), "w", encoding='utf-8') as file_write:
	json.dump(l, file_write, indent=4, sort_keys=True, ensure_ascii=False)
