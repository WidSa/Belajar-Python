# operator dalam bentuk method
# merubah case dari string

# Uppercase
salam = "hai"
print("Normal : " + salam)
upper = salam.upper()
print("Uppercase : " + upper)

# Lowercase
contoh = "Hey, Salam Kenal NamakU DWI"
print("Normal : " + contoh)
lower =  contoh.lower()
print("Lowercase : " + lower)

# pengecekkan dengan isX method
salam = "salam kenal"
is_lower = salam.islower()
print(salam + " is lower : " + str(is_lower))
is_upper = salam.isupper()
print(salam + " is upper : " + str(is_upper))

# isalpha() => untuk mengecek semua huruf
# isalnum() => untuk mengecek huruf dan angka
# isdecimal() => untuk mengecek angka saja
# isspace() => untuk spasi, tab, newline
# istitle() => untuk semua kata dimulai denganhuruf kapital/besar

judul = "Spongebob Square Pant"
is_title = judul.istitle()
print(judul + " is title : " + str(is_title))

# startswith() endswith() => check komponen awal atau akhri suatu kalimat
check_awal = "hey siapa kau ini".startswith("hey")
print("start : " + str(check_awal))

# penggabungan komponen => join() || pemisahaan komponen => split()
pisah = ["aku", "sayang", "dia"]
print(pisah)
gabung = ' '.join(pisah)
print(gabung)

gabungan = "diatfksayangtfkyangtfklain"
print(gabungan)
pemisah = gabungan.split('tfk')
print(pemisah)

# alokasi karakter => rjust(), ljust(), center() 
print('='*7 + ' Data ' + '='*7)
kanan = "kanan".rjust(10)
print("="+kanan+"=")
kiri = "kiri".ljust(10)
print('='+kiri+'=')
tengah = "tengah".center(10, '+')
print('='+tengah+'=')

# menghilangkan karakter => strip()
tengah = tengah.strip("+")
print('='+tengah+'=')
