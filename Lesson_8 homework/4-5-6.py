# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для
# классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для 
# приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение
# компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую 
# структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества 
# принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


#Сделано примитивно, не успевал :(

class Storage:
	items = {'Printer': 0, 'Scanner': 0, 'Copier': 0}

	def add_item(self, item):
		self.items[item.name] += item.qty
		print(f'{item.name} item was added to storage, qty: {item.qty}')

	def remove_item(self, item, qty):
		self.items[item] -= qty
		print(f'{item} item was removed from storage, qty: {qty}')

	def get_items(self):
		print(f'Current storage is:')
		for key, value in self.items.items():	
			print(f'{key}: {value}')

	def set_qty(self, item):
		if isinstance(item.qty, int):
			self.items[item.name] = item.qty
			print(f'{item.name} item qty was changed to: {item.qty}')
		else:
			raise TypeError

class Equipment:
	def __init__(self, qty):
		self.set_qty(qty)

	def set_qty(self, qty):
		if isinstance(qty, int):
			self.qty = qty
		else:
			raise TypeError


class Printer(Equipment):
	name = 'Printer'

class Scanner(Equipment):
	name = 'Scanner'

class Copier(Equipment):
	name = 'Copier'


storage = Storage()
storage.get_items()
storage.add_item(Printer(4))
storage.add_item(Scanner(6))
storage.remove_item('Printer', 2)
storage.add_item(Copier(16))
storage.set_qty(Scanner(22))
storage.get_items()