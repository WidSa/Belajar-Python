# Operasi Komparaso
# Setiap hasil dari operasi komparasi adalah boolean
#  >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2
c = 3

# lebih besar dari (>)
print("="*5,"Lebih Besar Dari (>)", "="*5)
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = c > 3
print(c, '>', 3, '=', hasil)

# Kurang dari (<)
print("="*5,"Kurang Dari (<)", "="*5)
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = c < 3
print(c, '<', 3, '=', hasil)

# Lebih Dari Sama Dengan (>=)
print("="*5,"Lebih Dari Sama Dengan (>=)", "="*5)
hasil = a >= 4
print(a, '>=', 4, '=', hasil)
hasil = b >= 4
print(b, '>=', 4, '=', hasil)
hasil = c >= 3
print(c, '>=', 3, '=', hasil)

# Kurang Dari Sama Dengan (<=)
print("="*5,"Kurang Dari Sama Dengan (<=)", "="*5)
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = c <= 3
print(c, '<=', 3, '=', hasil)

# Sama dengan (==)
print("="*5,"Sama Dengan (==)", "="*5)
hasil = a == 3
print(a, '==', 3, '=', hasil)
hasil = b == 3
print(b, '==', 3, '=', hasil)
hasil = c == 3
print(c, '==', 3, '=', hasil)

#  Tidak Sama dengan
print("="*5,"Tidak Sama Dengan (!=)", "="*5)
hasil = a != 3
print(a, '!=', 3, '=', hasil)
hasil = b != 3
print(b, '!=', 3, '=', hasil)
hasil = c != 3
print(c, '!=', 3, '=', hasil)

# 'IS' sebagai komparasi object identity
print("="*5, "Object Identity (IS)", "="*5)
x = 5 
y = 5 
z = 6
print('nilai x =', x, 'id: ', hex(id(x)))
print('nilai y =', y, 'id: ', hex(id(y)))
print('nilai z =', z, 'id: ', hex(id(z)))
hasil = x is y
print('x:', x, 'is', 'y:', y, hasil)
hasil = y is z
print('y:', y, 'is', 'z:', z, hasil)

# 'IS NOT'
print("="*5, "Object Identity (IS NOT)", "="*5)
x = 5 
y = 5 
z = 6
print('nilai x =', x, 'id: ', hex(id(x)))
print('nilai y =', y, 'id: ', hex(id(y)))
print('nilai z =', z, 'id: ', hex(id(z)))
hasil = x is not y
print('x:', x, 'is not', 'y:', y, hasil)
hasil = y is not z
print('y:', y, 'is not', 'z:', z, hasil)

