# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func_1(x,y):
		if x <= 0 or y >= 0:
			print("Введите действительное положительное число x и целое отрицательное число y")
		else:
			return x**y


def my_func_2(num, power):
		if num == 1 and power == 1:
			return num
		
		elif power == 0:
			return 1

		elif power < 0:
			counter = 1
			result = 1
			while counter <= abs(power):
				result *= num
				counter += 1
			return 1/result
		
		else:
			counter = 1
			result = 1
			while counter <= power:
				result *= num
				counter += 1
			return result

print(my_func_2(2,-3))