""""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
"""
#***********************************************
#***********************************************
#***********************************************
"""
у меня версия Python 3.8.1 x64, windows 10 x64

Рассматриваю функции нахождения  i-го простого числа:
Решето Эратосфена. 
    Получается самый затратный по ресурсам памяти алгоритм, т.к. хранит два списка. 
    При нахождении 125го простого числа внутренние переменные функции займут почти 15 кб.
    
Нахождение просто числа через перебор делителей.
    Средний по затратам памяти. Он хранит один список.
    Для нахождения 125го простого числа внутренние переменные функции занимают почти 5 кб.

Нахождение простого числа через квадратный корень.
    Занимает меньше всего памяти (56 байт), т.к. хранит всего две переменные, каждая из которых - целое число.

"""
import sys

# print(sys.platform, sys.version)
# win32 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)]

def show_sizeof(x, level=0):
    print("\t" * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)


def get_size(obj, seen=None):
    # From https://goshippo.com/blog/measure-real-size-any-python-object/
    # Recursively finds size of objects
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
      size += sum([get_size(v, seen) for v in obj.values()])
      size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
      size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
      size += sum([get_size(i, seen) for i in obj])
    return size


def sieve(n):
    count = n
    while True:
        _sieve = [i for i in range(count)] #сначала генерируем список чисел до n
        _sieve[1] = 0 # единица - не простое число
        for i in range(2, count): #удаляем из списка лишние числа
            if _sieve[i] != 0 :
                j = i ** 2
                while j < count:
                    _sieve[j] = 0
                    j += i
        primes = [i for i in _sieve if i != 0]
        if len(primes) >= n:
            break #если длина списка с простыми числами больше или равна n - этот список подходит, т.к. в нем есть n-ое по счету простое число
        else:
            count += n #иначе увеличим исходный список чисел, например на n, и повторим цикл
   
    #show_sizeof(count)
    #show_sizeof(_sieve)
    #show_sizeof(primes)
    
    vars_size = get_size(count) + get_size(_sieve) + get_size(primes) + get_size(n) + get_size(i) + get_size(j)

    return primes[n-1], vars_size




# для sieve(125)
# count - <class 'int'> 28 750
# _sieve - <class 'list'> 6224 [список из 750 элементов], где каждый элемент занимает 24 байта если это 0 и 28 в остальных случаях
# primes - <class 'list'> 1240 [список из 132 элементов], где каждый элемент занимает 28 байт
# плюс 84 байта на вспомогательные переменные (n, i, j)

print(sieve(125))
#(691, 14992)


def prime(n):
    count = n
    while True:
        primes = []
        for i in range(2, count): # генерируем список чисел от 2 до count
            for j in primes: # перебираем делители: найденные до этого простые числа (можно просто перебирать числа от 2 до i, но это еще больше увеличит время выполнения)
                if i % j == 0:
                    break
            else:
                primes.append(i) # добавляем число в список простых чисел

        if len(primes) >= n:
            break
        else:
            count += n
    #show_sizeof(count)
    #show_sizeof(primes)

    vars_size = get_size(count) + get_size(primes)# + get_size(n) + get_size(i) + get_size(j)

    return primes[n-1], vars_size

# prime(125)
# count - <class 'int'> 28 750
# primes - <class 'list'> 1240 [список из 132 элементов], где каждый элемент занимает 28 байт
# плюс 84 байта на вспомогательные переменные (n, i, j)

print(prime(125))
# (691, 5048)


def prime_sqrt(n):
    count = 1
    prime = 2

    while count < n:
        prime += 1
        for i in range(2, int(prime ** 0.5) + 1):
            if prime % i == 0:
                break
        else:
            count += 1
    #show_sizeof(count)
    #show_sizeof(prime)
    vars_size = get_size(count) + get_size(prime) + get_size(n) + get_size(i)

    return prime, vars_size


# prime_sqrt(125)
# count - <class 'int'> 28 125
# prime - <class 'int'> 28 691
# плюс 56 байт на вспомогательные переменные (n, i)

print(prime_sqrt(125))
# (691, 112)