# Width and Multiline

# Multiline
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44


# String Standar
data_string = f"Nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, Nomor Sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

#String Multiline (Dengan Menggunakan enter, Newline, \n)
data_string = f"Nama = {data_nama}, \nUmur = {data_umur}, \nTinggi = {data_tinggi}, \nNomor Sepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""Nama = {data_nama}
Umur = {data_umur}
Tinngi = {data_tinggi}
Sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# Mengatur Lebar
data_nama = "Ucup"
data_string = f"""
Nama   = {data_nama:>5}
Umur   = {data_umur:>5}
Tinngi = {data_tinggi:>5}
Sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)