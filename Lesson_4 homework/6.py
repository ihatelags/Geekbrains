# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию c() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо 
# предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

limit = 10
c = 0
for i in count(int(input('Введите первое число:\n'))):
	c += 1
	print(i)
	if i >= limit:
		c = 0
		break

l = [1, 2, 3]

print('\n','*'*25,'\n')

for i in cycle(l):
	c += 1
	print(i)
	if c >= limit:
		c = 0
		break