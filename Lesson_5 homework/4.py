# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

import os
path = os.path.join('files', '4.txt')
with open(path, 'r', encoding='utf-8') as file_read:
	lines = file_read.readlines()

with open(os.path.join('files', '4_rus.txt'), 'w', encoding='utf-8') as file_write:
	for line in lines:
		i = line.split()
		i[0] = dictionary[i[0]]
		print(' '.join(i), file=file_write)


from googletrans import Translator as gt
with open(os.path.join('files', '4_rus_gt.txt'), 'w', encoding='utf-8') as file_write:
	for line in lines:
		i = line.split()
		i[0] = gt().translate(i[0], dest = "ru").text.title()
		print(' '.join(i), file=file_write)

