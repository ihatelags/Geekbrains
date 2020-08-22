""""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена». Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""

""""
Функция с использоваием решета эратосфена выполняется значительно быстрее
"""

import cProfile
import timeit

def _timeit(func):
    return f'{timeit.timeit(func, number=100, globals=globals()):.5f}'

def sieve(n):
    end = n
    while True:
        _sieve = [i for i in range(end)] #сначала генерируем список чисел до n
        _sieve[1] = 0 # единица - не простое число
        for i in range(2, end): #удаляем из списка лишние числа
            if _sieve[i] != 0 :
                j = i ** 2
                while j < end:
                    _sieve[j] = 0
                    j += i
        primes = [i for i in _sieve if i != 0]
        if len(primes) >= n:
            break #если длина списка с простыми числами больше или равна n - этот список подходит, т.к. в нем есть n-ое по счету простое число
        else:
            end += n #иначе увеличим исходный список чисел, например на n, и повторим цикл
    return primes[n-1]

#print(sieve(10))

#print(_timeit('sieve(10)'))
#print(_timeit('sieve(100)'))
#print(_timeit('sieve(500)'))
print(_timeit('sieve(1000)'))
# 0.00156
# 0.07631
# 0.55229
# 1.14418

#cProfile.run('sieve(1000)')
# 28 function calls in 0.010 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#     1    0.008    0.008    0.010    0.010 Lesson4_task2.py:23(sieve)
#     8    0.001    0.000    0.001    0.000 Lesson4_task2.py:26(<listcomp>)
#     8    0.001    0.000    0.001    0.000 Lesson4_task2.py:34(<listcomp>)
#     1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#     8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def prime(n):
    count = n
    while True:
        primes = []
        for i in range(2, count): # генерируем список чисел от 2 до end
            for j in primes: # перебираем делители: найденные до этого простые числа (можно просто перебирать числа от 2 до i, но это еще больше увеличит время выполнения)
                if i % j == 0:
                    break
            else:
                primes.append(i) # добавляем число в список простых чисел

        if len(primes) >= n:
            break
        else:
            count += n

    return primes[n-1]

#print(prime(10))

# print(_timeit('prime(10)'))
# print(_timeit('prime(100)'))
# print(_timeit('prime(500)'))
print(_timeit('prime(1000)'))
# 0.00111
# 0.11183
# 3.15550
# 10.57353


#cProfile.run('prime(1000)')
# 4822 function calls in 0.104 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.104    0.104 <string>:1(<module>)
#     1    0.103    0.103    0.104    0.104 Lesson4_task2.py:57(prime)
#     1    0.000    0.000    0.104    0.104 {built-in method builtins.exec}
#     8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#  4810    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
