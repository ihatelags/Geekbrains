""""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
"""
from collections import deque


BASE = 16
HEX_NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')
BIN_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}


def sum_hex(num1, num2):
   
    if num1 != deque(num1):
        num1 = deque(num1)
    if num2 != deque(num2):
        num2 = deque(num2)


    if len(num2) > len(num1):
        num1, num2 = num2, num1

    num2.extendleft('0' * (len(num1) - len(num2)))

    result = deque()
    overflow = 0
    for i in range(len(num1) - 1, -1, -1):
        num1_number = BIN_NUMBERS[num1[i]]
        num2_number = BIN_NUMBERS[num2[i]]

        result_number = num1_number + num2_number + overflow

        if result_number >= BASE:
            overflow = 1
            result_number -= BASE
        else:
            overflow = 0

        result.appendleft(HEX_NUMBERS[result_number])

    if overflow == 1:
        result.appendleft('1')

    return list(result)


a = "a2"
b = "c4F"
# a = input('Введите первое число в hex формате (только цифры от 0 до f): ')
# b = input('Введите второе число в hex формате (только цифры от 0 до f): ')
a = a.upper()
b = b.upper()

print(f'{a} + {b} = {sum_hex(a, b)}')

print('Проверка:', hex(int(a, 16) + int(b, 16)).upper()[2:])