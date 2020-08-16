# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import os
path = os.path.join('files', '5.txt')

import random
with open(path, "w", encoding = "utf-8") as file:
	for i in range(random.randint(1,10)):
		num = random.randint(1,10)
		print(str(num), end =" ", file=file)

sum = 0
with open(path, "r", encoding = "utf-8") as file_read:
	for i in file_read.readlines():
		for j in i.split():
		 sum+=int(j)

print(sum)