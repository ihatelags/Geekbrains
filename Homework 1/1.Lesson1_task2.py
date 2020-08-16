""""
2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""
a = 5
b = 6
bit_and = a & b
bit_or = a | b
bit_xor = a ^ b
bit_not_a = ~a
bit_not_b = ~b
bit_shr_a_2 = a >> 2
bit_shl_a_2 = a << 2

print("a: {} or {}".format(a, bin(a)))
print("b: {} or {}".format(b, bin(b)))
print("a and b = {} or {}".format(bit_and, bin(bit_and)))
print("a or b = {} or {}".format(bit_or, bin(bit_or)))
print("a xor b = {} or {}".format(bit_xor, bin(bit_xor)))
print("not a = {} or {}".format(bit_not_a, bin(bit_not_a)))
print("not b = {} or {}".format(bit_not_b, bin(bit_not_b)))
print("a shr 2 = {} or {}".format(bit_shr_a_2, bin(bit_shr_a_2)))
print("a shl 2 = {} or {}".format(bit_shl_a_2, bin(bit_shl_a_2)))