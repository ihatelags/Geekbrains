""""
4. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

НЕ ПРОВЕРЯТЕСЯ:
начальное число/символ меньше конечного
для чисел - пользователь вводит числа
для символов - пользователь вводит символы единичной длины
"""
import random

text_int = "'int' - покажу случайное целое число"
text_float = "'float' - покажу случайное целое число"
text_symb = "'symb' - покажу случайный символ"
print("{}\n{}\n{}\nДля указанного диапазона".format(text_int, text_float, text_symb))
command = input("Введите команду: ")

if command == "int":
    a = int(input("Введите начальное значение диапазона: "))
    b = int(input("Введите конечное значение диапазона: "))
    print("{} - случайное целое число от {} до {}".format(random.randint(a,b),a,b))

elif command == "float":
    a = int(input("Введите начальное значение диапазона: "))
    b = int(input("Введите конечное значение диапазона: "))
    print("{} - случайное вещественное число от {} до {}".format(random.uniform(a, b), a, b))

elif command == "symb":
    a = input("Введите начальный символ диапазона: ")
    b = input("Введите конечный символ диапазона: ")
    print("{} - случайный символ от {} до {}".format(chr(random.randint(ord(a), ord(b))), a, b))
else:
    print("Неверная команда")