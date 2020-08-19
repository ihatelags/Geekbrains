""""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random
a = [random.randint(0,100) for _ in range(20)]
print(a)

index_min = 0
index_max = 0

for i in range(len(a)):
    if a[i] > a[index_max]:
        index_max = i
    elif a[i] < a[index_min]:
        index_min = i

a[index_max], a[index_min] = a[index_min], a[index_max]
print(f"{a}\n\nПоменяли местами элементы {a[index_max]} и {a[index_min]} c индексами {index_min} и {index_max}\n")