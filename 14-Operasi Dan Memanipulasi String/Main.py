# Operasi dan Manipusi String
# 1. menyambung string (concatenate)
nama_depan = "Budi"
nama_tengah = "Derwinta"
nama_belakang = "Wicaksono"

nama_lengkap = nama_depan + " " + nama_tengah + " " + nama_belakang
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. operator untuk string
# mengecek apakah terdapat char atau string di string

B = "B"
status = B in nama_lengkap
print("String " + B + " \nada di " + nama_lengkap + " = " + str(status))

B = "B"
status = B not in nama_lengkap
print("String " + B + " \ntidak ada di " + nama_lengkap + " = " + str(status))

print("="*25)

b  = "b"
status = b in nama_lengkap
print("String " + b + " \nada di " + nama_lengkap + " = " + str(status))

b  = "b"
status = b not in nama_lengkap
print("String " + b + " \ntidak ada di " + nama_lengkap + " = " + str(status))

print("="*10 + " Indexing " + "="*10)
# indexing 
print(nama_lengkap)
print("index ke-0 : " + nama_lengkap[0])
print("index ke-10 : " + nama_lengkap[10])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-7) : " + nama_lengkap[-7])
print("index ke-[0, 4] : " + nama_lengkap[0:4])
print("index ke-[5, 13] : " + nama_lengkap[5:13])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

acii_code_spasi = ord(" ")
print("ASCII code untuk spasi adalah : " + str(acii_code_spasi))
acii_code_W = ord("W")
print("ASCII code untuk W adalah : " + str(acii_code_W))

# 4. operator dalam bentuk method
data = "kasur rusak ancur sekali"
jumlah = data.count("k")
print("jumlah k pada\n" + data + " : " + str(jumlah))

