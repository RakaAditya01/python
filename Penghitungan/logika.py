# Operasi Logika atau Boolean

# not, or, and, xor

# NOT
print('======NOT=====')
a = False
c = not a
print('data a =', a)
print('---------- NOT')
print('data c =', c)

# OR (Jika Salah satu TRUE maka hasilnya adalah TRUE)
print('======OR=====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)
a = True
b = False
c = a or b
print(a, ' OR', b, '=', c)
a = True
b = True
c = a or b
print(a, ' OR', b, ' =', c)

# AND (Jika dua buah nilai TRUE, maka hasilnya TRUE)
print('======AND=====')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)
a = True
b = False
c = a and b
print(a, ' AND', b, '=', c)
a = True
b = True
c = a and b
print(a, ' AND', b, ' =', c)

# XOR (akan TRUE jika salah satu TRUE, sisanya FALSE)
print('======XOR=====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)
a = True
b = False
c = a ^ b
print(a, ' XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, ' XOR', b, ' =', c)