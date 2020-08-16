# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
	def __init__(self, str_date):
		self.str_date = str(str_date)

	@classmethod
	def extract(cls, str_date):
		date = []

		for i in str_date.split('-'):
			date.append(i)

		return int(date[0]), int(date[1]), int(date[2])

	@staticmethod
	def valid(day, month, year):

		if 1 <= day <= 31 and int(day) == day:
			if 1 <= month <= 12 and int(month) == month:
				if 9999 >= year >= 0 and int(year) == year:
					return f'Дата прошла валидацию'
				else:
					return f'Неправильный год'
			else:
				return f'Неправильный месяц'
		else:
			return f'Неправильный день'

	def __str__(self):
		return f'Текущая дата {Date.extract(self.str_date)}'


today = Date('22-4-2002')
print(today)
print(Date.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Date.extract('11-11-2011'))
print(today.extract('11-11-2020'))
print(Date.valid(1, 11, 2000))