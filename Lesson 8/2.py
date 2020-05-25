# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class HandleDivisionByZero(Exception):
	def __init__(self, txt):
		self.txt = txt

try:
	x = float(input('Делимое? '))
	y = float(input('Делитель? '))
	if not y or y == 0:
		raise HandleDivisionByZero('Error: division by zero')
	print(f'Результат: {x/y}')

except ValueError:
	print('Были введены нечисловые значения')
except HandleDivisionByZero as error:
	print(error)