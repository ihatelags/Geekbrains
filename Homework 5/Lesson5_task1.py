""""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. 
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
import collections as cs
companies_dict = cs.OrderedDict()
annual_incomes = cs.Counter()

n = int(input("Какое количество предприятий будете вводить? "))

for i in range(n):
    name = input(f"Введите название {i + 1} предприятия: ")
    incomes = [None] * 4
    for j in range(4):
        incomes[j] = int(input(f"Введите доход за {j+1} квартал для этого предприятия: "))
        annual_incomes[name] += incomes[j]
    companies_dict[name] = incomes

print(companies_dict, annual_incomes, sep="\n")

average_income = sum(annual_incomes.values())/n
lower = sorted([key for key, value in annual_incomes.items() if value < average_income])
greater = sorted([key for key, value in annual_incomes.items() if value > average_income])

print(f"Среднегодовая прибыль по всем предприятиям: {average_income}")
print(f"Предприятия, чей годовой доход выше среднего: {greater}")
print(f"Предприятия, чей годовой доход ниже среднего: {lower}")



