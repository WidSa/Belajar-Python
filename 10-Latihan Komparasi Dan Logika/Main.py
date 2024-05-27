# Latihan Komparasi Dan Logika
# Membuat Gabungan area rentang dari angka

# +++++3-------7+++++

# inputUser = float(input("Masukkan angka yang bernilai kurang dari 3\natau \nlebih besar dari 7\n:"))

# # +++++3-----
# # memeriksa angka kurang dari 3 
# isKurangDari = (inputUser < 3)
# print("Kurang dari 3:", isKurangDari)

# # -------7++++++
# isLebihDari = (inputUser > 7)
# print("Lebih dari 7:", isLebihDari)

# # +++++3-------7++++++
# isCorrect = isKurangDari or isLebihDari
# print("Angka yang anda masukkan: ", isCorrect)

# # -----3++++++7------
# print('='*10)
# inputUser = float(input("Masukkan angka yang bernilai lebih dari 3\ndan \nkurang besar dari 7\n:"))

# # -----3++++++
# isLebihDari =  (inputUser > 3)
# print("Lebih dari 3:", isLebihDari)

# # +++++7-----
# isKurangDari = (isKurangDari < 7)
# print("Kurang dari 7:", isKurangDari)

# # -----3+++++++7------
# isCorrect =  isLebihDari and isKurangDari
# print("Angka yang anda masukkan: ", isCorrect)

# -----0++++++5------8++++++11------
print('='*10)
inputUser = float(input("Masukkan angka Kisaran 0-5 dan 8-11: "))

# -----0+++++++5------
isKurangDari = (inputUser > 0 and inputUser < 5)
print("Kisaran 0-5:", isKurangDari)

# ------8+++++++11-----
isLebihDari = (inputUser > 8 and inputUser < 11)
print("Kisaran 8-11:", isLebihDari)

# -----0++++++5------8++++++11------
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan: ", isCorrect)


# +++++0------5++++++8------11++++++
