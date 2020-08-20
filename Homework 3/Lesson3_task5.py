""""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random
a = [random.randint(-100,10) for _ in range(20)]
b = [random.randint(-10,20) for _ in range(20)]

def max_negative(array):
	i = 0
	index = -1
	for i in range(len(array)):
		if array[i] < 0 and index == -1:
			index = i
		elif 0 > array[i] > array[index]:
			index = i
		i += 1

	return array[index] if index != -1 else None



print(a)
print("Для массива a максимальный отрицательный элемент: {}\n".format(max_negative(a)))
print(b)
print("Для массива b максимальный отрицательный элемент: {}".format(max_negative(b)))