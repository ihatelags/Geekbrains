""""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""
a = [i for i in range(2,100)]
b = [i for i in range(2,10)]

#ответы сложу в словарь
dict_ab = {i : 0 for i in range(2,10)}

for ela in a:
    for elb in b:
        count_el = dict_ab[elb]
        if ela % elb == 0:
            count_el +=1
            dict_ab[elb] = count_el

for key, value in dict_ab.items():
    print(f"Числу {key} кратно {value} чисел")