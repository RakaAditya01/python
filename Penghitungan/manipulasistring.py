# Operasi dan Manipulasi String

# 1. Menyambung String (contatenate)
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama +" "+ nama_tengah +"'"+ nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang String
panjang = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + "=" + str(panjang))

# 3. Operator Untuk String

# mengecek apakah ada komponen char atau string di string

d = "d"
status  = d in nama_lengkap
print(d + " ada di " +nama_lengkap +" = "+ str(status))

D = "D"
status  = D in nama_lengkap
print(D + " ada di " +nama_lengkap +" = "+ str(status))

d = "d"
status  = d not in nama_lengkap
print(d + " tidak ada di " +nama_lengkap +" = "+ str(status))

# mengulang String
print("wk"*10)
print(15*"wk")

# Indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("Index ke-[0:3] :" + nama_lengkap[0:3]) # : adalah sampai
print("Index ke-[3:7] :" + nama_lengkap[3:8]) # : adalah sampai
print("Index ke-[0,2,4,6,8,10] :" + nama_lengkap[0:10:2]) # : adalah sampai

# Item paling Kecil
print("paling Kecil : " + min(nama_lengkap))
# Item paling Besar
print("paling Besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII CODE untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. Operator dalam bentuk Method

data = "radit dimas"
jumlah = data.count("i")
print("jumlah i pada " + data + " = " + str(jumlah))