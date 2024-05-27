# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

a = 5 # Adalah Assignment
print("Nilai A: ", a)

a += 1 # artinya adalah a = a + 1
print("Nilai A += 1, nilai A menjadi: ", a)

a -= 2 # artinya adalah a = a - 2
print("Nilai A -= 2, nilai A menjadi: ", a)

a *= 5 # artinya adalah a = a * 5
print("Nilai A *= 5, nilai A menjadi: ", a)

a /= 4 # artinya adalah a = a / 4
print("Nilai A /= 4, nilai A menjadi: ", a)

a **= 2 # artinya adalah a = a ** 2
print("Nilai A **= 2, nilai A menjadi: ", a)

a //= 2 # artinya adalah a = a // 2
print("Nilai A //= 2, nilai A menjadi: ", a)

a %= 7 # artinya adalah a = a % 7
print("Nilai A %= 7, nilai A menjadi: ", a)

# Operasi Bitwise
# OR
print('='*6, 'OR', '='*6)
C = True
print("\nNilai C:", C)

C |= False
print("Nilai C |= False, Nilai C menjadi:", C)

C = False
print("\nNilai C:", C)

C |= False
print("Nilai C |= False, Nilai C menjadi:", C)

# AND 
print('='*6, 'AND', '='*6)
C = True
print("\nNilai C:", C)

C &= True
print("Nilai C &= True, Nilai C menjadi:", C)

C = False
print("\nNilai C:", C)

C &= False
print("Nilai C &= False, Nilai C menjadi:", C)

# XOR
print('='*6, 'XOR', '='*6)
C = True
print("\nNilai C:", C)

C ^= True
print("Nilai C ^= True, Nilai C menjadi:", C)

C = False
print("\nNilai C:", C)

C ^= True
print("Nilai C ^= True, Nilai C menjadi:", C)

