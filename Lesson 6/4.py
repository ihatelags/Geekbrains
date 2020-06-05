# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
# Выполните вызов методов и также покажите результат.

class Car:

	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		print(f'{self.name} поехала')

	def stop(self):
		print(f'{self.name} остановилась')

	def turn(self, direction):
		self.direction = direction
		print(f'{self.name} повернула {self.direction}')

	def show_speed(self):
		print(f'Скорость машины {self.name}: {self.speed}')


class TownCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)


	def show_speed(self):
		if self.speed > 40:
			print(f'Скорость машины {self.name}: {self.speed}. Скорость превышена!')
		else:
			print(f'Скорость машины {self.name}: {self.speed}')

class SportCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)


class WorkCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		if self.speed > 60:
			print(f'Скорость машины {self.name}: {self.speed}. Скорость превышена!')
		else:
			rint(f'Скорость машины {self.name}: {self.speed}')

class PoliceCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)


sport = SportCar(100, 'черная', 'BMW', False)
town = TownCar(40, 'белая', 'Toyota', False)
work = WorkCar(70, 'зеленая', 'Ferrari', False)
police = PoliceCar(110, 'синяя',  'Mazda', True)


town.turn('налево')
sport.turn('направо'), sport.stop()
work.go()
work.show_speed()
print(f'{work.name} {work.color}')
sport.show_speed()
town.show_speed()
police.show_speed()
