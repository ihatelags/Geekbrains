""""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
"""

""""
Рассматривается алгоритм, который считает сумму ряда (-1/2)^n до n
* рекурсивно
* через геометрическую прогрессию
* через цикл for

Вывод: Вариант с прогрессией самый быстрый, т.к. происходит только одно вычисление - итоговая сумма, без вычисления каждого члена ряда.
"""


import cProfile
import timeit

def _timeit(func):
	return f'{timeit.timeit(func, number=100, globals=globals()):.5f}'

def test_func(func):
    """ Тест реализаций
    """
    sum_5 = [1, 0.5, 0.75, 0.625, 0.6875]
    for i in range(5):
        if round(func(i+1), 4) == sum_5[i]:
            print(f'TEST {i+1} - OK')
        else:
            print(f'TEST {i+1} - ERROR')
    print()

#сумма через рекурсию
def sum_rec(n):
    if n == 1:
        return 1
    return (-0.5) ** (n-1) + sum_rec(n-1)

#геометрическая прогрессия
def sum_geom(n):
    b1 = 1
    q = -0.5
    s = (b1 * (1-q**n)) / (1 - q)
    return s


# сумма через цикл for
def sum_cycle(n):
    sum_series = 1
    if n > 1:
        prev = 1
        for _ in range(1, n):
            current = prev * -0.5
            sum_series += current
            prev = current
    return sum_series


# Тестируем реализации
#test_func(sum_rec)
#test_func(sum_geom)
#test_func(sum_cycle)




#********************************************************************************
print('Рекурсия')
print(_timeit('sum_rec(5)')) # 0.00016
print(_timeit('sum_rec(100)')) # 0.00313
print(_timeit('sum_rec(500)')) # 0.01917
print(_timeit('sum_rec(950)')) # 0.03351


cProfile.run("sum_rec(950)")
# 754 function calls (4 primitive calls) in 0.001 seconds
# 951/1    0.001    0.000    0.001    0.001 Lesson4_task1.py:28(sum_rec)

#********************************************************************************
print('Прогрессия')
print(_timeit('sum_geom(5)')) # 0.00004
print(_timeit('sum_geom(100)')) # 0.00004
print(_timeit('sum_geom(500)')) # 0.00004
print(_timeit('sum_geom(950)')) # 0.00004

cProfile.run("sum_geom(950)")
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 Lesson4_task1.py:45(sum_geom)


#********************************************************************************
print('Цикл')
print(_timeit('sum_cycle(5)')) # 0.00007
print(_timeit('sum_cycle(100)')) # 0.00068
print(_timeit('sum_cycle(500)')) # 0.00350
print(_timeit('sum_cycle(950)')) # 0.00689


cProfile.run("sum_cycle(950)")
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 Lesson4_task1.py:102(sum_cycle)


#********************************************************************************
print('Рекурсия 	Прогрессия 	Цикл')
print(_timeit('sum_rec(950)'), '        ', _timeit('sum_geom(950)'), '	', _timeit('sum_cycle(950)'))
#result: 0.03813          0.00004         0.00689

    