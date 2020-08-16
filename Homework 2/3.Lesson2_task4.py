""""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""
def sum_recursion(n):
    return (-0.5) ** (n-1) + sum_recursion(n-1) if n > 1 else 1

def sum_for(n):
    sum = 0
    for i in range(n):
        sum += (-0.5) ** i
    return sum

def sum_while(n):
    sum = 0
    i = 0
    while i < n:
        sum += (-0.5) ** i
        i += 1
    return sum

number = int(input("Введите количество элементов для ряда: "))
text = "Сумма ряда через"
print(f"{text} рекурсию {sum_recursion(number)}\n{text} цикл for {sum_for(number)}\n{text} цикл while {sum_while(number)}")