# Operasi Aritmatika

a = 10
b = 3

# Operasi Tambah (+)
hasil = a + b
print(a, '+', b, '=', hasil)

# Operasi Kurang (-)
hasil = a - b
print(a, '-', b, '=', hasil)

# Operasi Per-Kalian (*)
hasil = a * b
print(a, '*', b, '=', hasil)

# Operasi Pembagian (/)
hasil = a / b
print(a, '/', b, '=', hasil)

# Operasi Eksponen (pangkat) (**)
hasil = a ** b
print(a, '**', b, '=', hasil)

# Operasi modulus (sisa pembagian) (%)
hasil = a % b
print(a, '%', b, '=', hasil)

# Operasi Floor division (//)
hasil = a // b
print(a, '//', b, '=', hasil)



# Prioritas Operasi, Operational Precedence
# Urutan Perhitungan
# ()
# Exponen **
# Perkalian dan teman teman * / ** % //
# Pertambahan dan pengurangan + -

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x , '/', y, '-', y, '%', z, '//', x, '=', hasil)

hasil = x + y * z
print(x, '+', y, '*', z, '=', hasil)
# Kurung Mengambil Langkah Paling Pertama
hasil = (x + y) * z
print( '(', x, '+', y, ')*', z, '=', hasil)