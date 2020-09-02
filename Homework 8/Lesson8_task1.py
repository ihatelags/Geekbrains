""""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""

def count_subsrtings(input_string):
    hash_set = set()

    window = len(input_string) - 1

    while window > 0:

        for i in range(len(input_string) - window + 1):
            hash_set.add(hash(input_string[i:i + window]))

        window -= 1

    return len(hash_set)


string = input('Введите строку: ')
print(f'В строке "{string}" содержится {count_subsrtings(string)} уникальных подстрок')