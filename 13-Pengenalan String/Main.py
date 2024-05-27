#  String

data = 'ini adalah String'
print(data)
print(type(data))

# Menggunakan single quote
data = 'Menggunakan single quote'
print(data)

# Menggunakan double qoute
data = "Mengunakan duoble qoute"
print(data)

# Dengan backslash (\)
print('Besok adalah hari jum\'at')
print('g\'day, isn\'t it? ')

# backslash
print("C:\\user\\Andi")

# Tab
print("Andi\tDirmansha")

# backspase
print("Ando \bCeoll")

# newline
print("Baris pertama, \nBaris Kedua")  # LF => Line Feed -> Unix, macOs, Linux
print("Baris satu. \rBaris dua")       # CR => Carriage Return -> Commadore ,acorn ,lisp
print("Baris kesatu. \r\nBaris Kedua") # CRLF => Line Feed Carriage Return -> Windows

# String Literal
# print("C:\new folder") # Akan salah pada pathnya

# menggunakan RAW String
print(r"C:\new folder")

# Multiline
print("""
    Nama: Andi Dernata,
    Umur: 27
    media sosial: Andi_Darna
""")
