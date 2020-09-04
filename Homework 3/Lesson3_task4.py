""""
4. Определить, какое число в массиве встречается чаще всего.

если несколько чисел встречаются одинаковое количество раз, то алгоритм оставит первое встреченное
для проверки подсчет всех уникальных элементов записывается в словарь
"""
import random
a = [random.randint(0,10) for _ in range(30)]
a_unique = list(set(a))

number = None
max_count = 0
dict_counts = {}
for element in a_unique:
    dict_counts[element] = a.count(element)
    element_count = a.count(element)
    if element_count > max_count:
        max_count = element_count
        number = element

print(a)
print()
print(dict_counts)
print(f"\nЧисло {number} встречается {max_count} раз\n")


