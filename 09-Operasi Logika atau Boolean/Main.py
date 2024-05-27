# Operasi Logika atau Boolean
# not, or, and, xor

print('='*6, 'NOT', '='*6)
a = True
c = not a
print('Data A:', a)
print('-'*7, 'Not')
print('Data C:', c)

# OR (Jika Salah Satu True Maka Hasilnya Akan TRue)
print('='*6, 'OR', '='*6)
a = True
b = False
Hasil = a or b
print(a, ' OR', b, ' :', Hasil)
Hasil = a or a 
print(a, ' OR', a,'  :', Hasil)
Hasil = b or b 
print(b, 'OR', b, ':' , Hasil)
Hasil = b or a 
print(b, 'OR', a, ' :' , Hasil)

# AND ( jIKA Kedua Nilai Data Harus TRUE Maka Hasinya Akan TRUE Selain Itu Akan FALSE)
print('='*6, 'AND', '='*6)
a = True
b = False
Hasil = a and b
print(a, ' AND', b, ' :', Hasil)
Hasil = a and a 
print(a, ' AND', a,'  :', Hasil)
Hasil = b and b 
print(b, 'AND', b, ':' , Hasil)
Hasil = b and a 
print(b, 'AND', a, ' :' , Hasil)

# XOR (Akan TRUE Jika Salah satu True, Selain itu akan False)
print('='*6, 'XOR', '='*6)
a = True
b = False
Hasil = a ^ b
print(a, ' XOR', b, ' :', Hasil)
Hasil = a ^ a 
print(a, ' XOR', a,'  :', Hasil)
Hasil = b ^ b 
print(b, 'XOR', b, ':' , Hasil)
Hasil = b ^ a 
print(b, 'XOR', a, ' :' , Hasil)

