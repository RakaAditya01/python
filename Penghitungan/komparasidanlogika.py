# logika dan Komparasi

# Membuat gabungan area rentang dari angka

# ++++++++3-------10++++++++

inputUser  = float(input("Masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))

# +++++++3-----------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3 )
print("Kurang dari 3 = ", isKurangDari)

#---------------------10+++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# ++++++++3-------10++++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan: ", isCorrect)

# ---------3+++++++++10--------
# Kasus Irisan
print("\n",10*"=","\n")
inputUser  = float(input("Masukan angka yang bernilai\n Lebih dari 3\ndan\n Kurang besar dari 10\n:"))

#---------3+++++++++
# Lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 =", isLebihDari)

#++++++++++10----------
isKurangDari = inputUser < 10
print("Kurang Dari 10 =", isKurangDari)

# ---------3+++++++++10--------
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukan: ", isCorrect)


# ------0++++++++++++5------------8+++++++++11--------
print("\n",10*"=","\n")
inputUser = float(input("Masukan angka :"))

print("true") if (inputUser > 0 and inputUser < 5) or (inputUser > 8 and inputUser < 11) else print("false") 

# +++++++0-----------5++++++++8------------11++++++
print("\n", 10*"=", "\n")
inputUser = float(input("masukan angka :"))
print("false") if (inputUser < 0 and inputUser > 5) or (inputUser < 8 and inputUser > 11) else print("false")