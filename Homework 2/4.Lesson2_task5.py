""""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""

code = 32
while code <= 127:
    s = ""
    for i in range(10):
        s = s + f"{code} - {chr(code)}; " if code <= 127 else s + ""
        code += 1
    print(s)