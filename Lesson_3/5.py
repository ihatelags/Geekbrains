# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. 
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет 
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. 
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def calculate_sum(*args):
	sum = 0
	check = False
	for element in args:
		try:
			sum += float(element)
		except ValueError:
			check = True
	return sum, check


sum_output = float()

while True:
	numbers_string = input('Введите список чисел через пробел или не число для выхода: ').split(' ')
	sum, stop_flag = calculate_sum(*numbers_string)
	sum_output += sum
	print(f'сумма {sum_output}')

	if stop_flag:
		break