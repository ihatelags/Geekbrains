# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

l = ['a', 1, {'a', 2}, 3.1, ['11','aa'], {'aa':'zz'}, (41.12, 121)]
for i in l:
	print(f'Элемент {i}, {type(i)}')
	if type(i) == list or type(i) == tuple or type(i) == dict:
		for j in i:
			print(f'Элемент {j} внутри {i}, {type(j)}')
	print()