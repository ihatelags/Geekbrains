# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

import os

path = os.path.join('files', '1.txt')

try:
	file = open(path, "w", encoding="utf-8")
	while True:
		content = input('Input: ')
		if content == "":
			break
		file.write(content + "\n")
except IOerror:
	print('Input/output error!')
finally:
	file.close()
