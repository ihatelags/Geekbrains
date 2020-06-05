# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать 
# формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
	def __init__(self, _length, _width):
		self._length = _length
		self._width = _width

	def mass(self, thickness):
		asph_mass_1sqm = 25
		asph_mass = self._length * self._width * asph_mass_1sqm * thickness
		return asph_mass/1000


length = 5000
width = 20
thickness = 5
road = Road(length, width)
print((f'Масса асфальта равна {road.mass(thickness)} тонн'))