""""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

def max_sum(n_numbers):
    """"
    Среди введенного количества n натуральных чисел находит наибольшее по сумме цифр.
    Возвращает число и сумму его цифр.
    """

    max_sum = 0
    max_number = 0

    for i in range(n_numbers):
        number = input(f"Введите число номер {i + 1}: ")
        sum_digits = 0
        for element in number:
            sum_digits += int(element)
        if sum_digits > max_sum:
            max_sum = sum_digits
            max_number = int(number)
    return max_number, max_sum

number, sum = max_sum(int(input("Сколько чисел вы хотите ввести? ")))
print(f"Наибольшее число по сумме его цифр - {number}. Сумма его цифр - {sum}")