"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
def my_encode(data):
    return [i.encode('utf-8') for i in data]

def my_decode(data):
    return [i.decode('utf-8') for i in data]

data = ['paзpaбoткa', 'aдминиcтpиpoвaниe', 'protocol', 'standard']

print(data)
print()
print(my_encode(data))
print()
print(my_decode(my_encode(data)))