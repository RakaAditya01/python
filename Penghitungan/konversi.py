# Latihan Konversi satuan Temperature

# Program Konversi Celcius ke satuan Lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam celcius :'))
print('suhu adalah = ', celcius, "Celcius")

# Reamur
reamur = (4/5) * celcius
print('suhu dalam reamur adalah = ', reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print('suhu dalam fahrenheit adalah = ', fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print('suhu dalam Kelvin adalah = ', kelvin, "Kelvin")