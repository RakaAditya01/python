# Format String

# Contoh Generic
# String
nama = "Raka"
format_str = f"hello {nama}"
print(format_str)

# Boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# Angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# Bilangan Bulat
angka = 15
format_str = f"bilangan bulat = {angka}"
print(format_str)

# Bilngan dengan Ordo Ribuan
angka = 2000
format_str = f"Ribuan = {angka:,}"
print(format_str)

# Bilangan Decimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}"
print(format_str)

# Menampilkan leading Zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# Menampilkan Tanda + atau -
angka_minus = -10
angka_plus  = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus  = f"plus  = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# Memformar Persen
persentase = 0.045
format_persen = f"Persen = {persentase:.2%}"

print(format_persen)

# Melakukan Operasi Aritmatika Di dalam Place Holder
harga = 10000
jumlah = 5

format_string = f"Harga Total = Rp. {harga*jumlah:,}"
print(format_string)

# Format angka Lain (Binary, Octal, Hexadecimal)

angka = 255
format_binary = f"Binary = {bin(angka)}"
format_octal  = f"Octal  = {oct(angka)}" 
format_hex    = f"Hex    = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)