# Operasi Komparasi

# Setiap Hasil dari operasi komparasi adalah Boolean

# >, <, >=, <=, ==, !=, is, is not 

a = 4
b = 2

# Lebih besar dari (>)
print('=====LEBIH BESAR (>)=====')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# Kurang dari (<)
print('=====KURANG DARI (<)=====')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# Lebih Dari Sama Dengan (>=)
print('===== LEBIH DARI SAMA DENGAN (>=)=====')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# Kurang Dari Sama Dengan (>=)
print('===== KURANG DARI SAMA DENGAN (<=)=====')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# Sama Dengan (==)
print('===== SAMA DENGAN (==)=====')
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

# Tidak Sama Dengan (!=)
print('===== TIDAK SAMA DENGAN (!=)=====')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

# Sama Dengan (==)
print('===== SAMA DENGAN (==)=====')
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

# 'is' sebagai komparasi objek identitiy
print('===== OBJECT IDENTITY (is)=====')
x = 5 # ini adalah assignment membuat objek 
y = 5
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

x = 5 # ini adalah assignment membuat objek 
y = 6
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

# 'is not'
print('===== OBJECT IDENTITY (is not)=====')
x = 5 # ini adalah assignment membuat objek 
y = 5
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is not y
print('x is y = ', hasil)

x = 5 # ini adalah assignment membuat objek 
y = 6
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is not y
print('x is y = ', hasil)