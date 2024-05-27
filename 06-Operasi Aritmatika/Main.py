# Operasi Aritmatika

a = 10
b = 2

# operasi penambahan
hasil = a + b 
print(a, '+', b, '=', hasil)

# operasi pengurangan
hasil = a - b 
print(a, '-', b, '=', hasil)

# operasi perkalian
hasil = a * b 
print(a, 'X', b, '=', hasil)

# operasi pembagian
hasil = a / b 
print(a, '/', b, '=', hasil)

# operasi eksponen (pengkat)
hasil = a ** b 
print(a, '^', b, '=', hasil)

# operasi modulus (sisa pembagian)
hasil = a % b 
print(a, '%', b, '=', hasil)

# operasi floor division
hasil = a // b 
print(a, '//', b, '=', hasil)

# prioritas operasi

x = 3
y = 5
z = 2

hasil = y ** z / x + y // z - x % z * x
print(y, '**', z, '/', x, '+', y, '//', z, '-', x, '%', z, '*', x, '=', hasil)