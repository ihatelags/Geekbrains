# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def coat_fabric(self):
		return round(self.width / 6.5 + 0.5, 2)

	def jacket_fabric(self):
		return round(self.height * 2 + 0.3, 2)

	@property
	def fabric(self):
		return str(f'Количество ткани: {round((self.coat_fabric()) + (self.jacket_fabric()), 2)}')


class Coat(Clothes):
	def __init__(self, width, height):
		super().__init__(width, height)
		self.fabric_amount_c = round(self.coat_fabric(), 2)

	def __str__(self):
		return f'Количество ткани для пальто {self.fabric_amount_c}'


class Jacket(Clothes):
	def __init__(self, width, height):
		super().__init__(width, height)
		self.fabric_amount_j = round(self.jacket_fabric(), 2)

	def __str__(self):
		return f'Количество ткани для костюм {self.fabric_amount_j}'

coat = Coat(4, 6)
jacket = Jacket(4, 8)
print(coat)
print(jacket)
print(coat.fabric)
print(jacket.fabric)
print(jacket.coat_fabric())
print(jacket.jacket_fabric())