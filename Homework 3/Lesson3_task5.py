""""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random
a = [random.randint(-100,10) for _ in range(20)]
b = [random.randint(-2,20) for _ in range(20)]

def max_negative(list):
    number = 0
    for element in list:
        if element < number:
            number = element
    return number if number < 0 else None

print(a)
print("Для массива a максимальный отрицательный элемент: {}\n".format(max_negative(a)))
print(b)
print("Для массива b максимальный отрицательный элемент: {}".format(max_negative(b)))