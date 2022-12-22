data = "ini adalah string"
print(data)
print(type(data))

# 1.Cara membuat String

'''
    1. dengan menggunakan single quote '...'
    2. degan menggunakan doublr quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = "Menggunakan Double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# Backslash
print("C:\\user\\Ucup")

# tab
print("ucup\totong, jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.")  # LF -> Line Feed -> unix, MacOs, Linux
print("baris pertama.\rbaris kedua.")  # CR -> Carriage Return -> Commodore, Acorn, Lisp
print("baris pertama.\r\nbaris kedua") # CRLF -> Line Feed Carriage Return -> dipakai oleh windows

# 3. String Literal atau raw

# hati-hati
print('C:\nnew folder') # akan salah pathnya

# menggunakna raw string
print(r'C:\new folder')

# multiline Literal String
print("""
Nama  : Ucup
Kelas : 3 SD
""")

# Multiline Literal String dan Raw
print(r"""
Nama  : Ucup
Kelas : 3 SD
Website : www.ucup.com/newID
""")