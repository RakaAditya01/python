# Operator daldm bentuk methods

## merubah case dari string

# merubah semua ke UpperCase

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke LowerCase
alay = "aKu KeCe AbieeZZZzzZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX Method

# contoh untuk pengecekan lower Case
salam = "sist"
apakah_lower = salam.islower() # Hasilnya Boolean
print(salam + " is Lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # Hasilya Boolean
print(salam + " is Upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <--semua kata dimulai dengan huruf besar

judul = "It Is Okay To Be Orkay" # istitle
cek_judul = judul.istitle() # hasilnya boolean

print(judul + " is title = " + str(cek_judul))

## ngecek Komponen startswith() endsswith()
cek_start = "Sangjangnim Oppa".startswith("sangjangnim")
print("Start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("End = " + str(cek_end))

## Penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = 'akuehmsayangehmkamu'
print(gabung.split('ehm'))

## alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip("-") # Menghilangkan tanda -
print("'"+tengah+"'")