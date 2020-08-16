""""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843
"""

def reverse(numbers):
    reverse_numbers = ""
    for number in str(numbers):
        reverse_numbers = number + reverse_numbers
    return reverse_numbers

print(reverse(input("Введите число: ")))

