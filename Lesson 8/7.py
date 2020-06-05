# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и 
# умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение 
# созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.z = 'a + b * i'

	def __add__(self, other):
		return f'z = {self.a + other.a} + {self.b + other.b} * i'

	def __mul__(self, other):
		return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

	def __str__(self):
		return f'z = {self.a} + {self.b} * i' if self.b > 0 else f'z = {self.a} - {-self.b} * i'


x = ComplexNumber(1, -3)
y = ComplexNumber(3, 4)
print(x)
print(x + y)
print(x * y)
