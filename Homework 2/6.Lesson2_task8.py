""""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

n_numbers = int(input("Сколько чисел вы хотите ввести? "))
search_digit = int(input("Какую цифру необходимо посчитать? "))
sum_digit = 0
for i in range(n_numbers):
    for element in input(f"Введите число номер {i+1}: "):
        sum_digit += 1 if int(element) == search_digit else 0

print(f"Цифра {search_digit} встретилась {sum_digit} раз")
