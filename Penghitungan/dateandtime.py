# Date and Time (latihan)

import datetime as dt

#hari_ini = dt.date.today()

#print(hari_ini)
#print(f"Hari ini Adalah Hari = {hari_ini:%A}")

#tanggal = dt.date(2005,5,25)
#print(tanggal)
#print(f"Hari ini Adalah Hari = {tanggal:%A}")

print("Silahkan Masukan Tanggal, \nBulan dan Tahun lahir Anda \n")
tanggal = int(input("Tanggal \t: "))
bulan   = int(input("Bulan \t\t: "))
tahun   = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal Lahir Anda adalah = {tanggal_lahir:}")

hari_ini = dt.date.today()
print(f"Hari Ini Tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Hari nya Adalah = {tanggal_lahir:%A}")
print(f"Umur Anda Adalah: {umur_tahun} Tahun, {umur_bulan_sisa} Bulan")