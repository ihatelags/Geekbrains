""""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
a = [random.randint(0,100) for _ in range(10)]

index_min = 0
index_max = 0

for i in range(len(a)):
    if a[i] > a[index_max]:
        index_max = i
    elif a[i] < a[index_min]:
        index_min = i

my_sum = 0

if index_min < index_max:
    for i in range(index_min+1, index_max):
        my_sum += a[i]
else:
    for i in range(index_max+1, index_min):
        my_sum += a[i]

print(f"Сумма между {index_min} и {index_max} элементами в массиве {a} равна {my_sum}\n")