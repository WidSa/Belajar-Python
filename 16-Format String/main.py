# Format String

# Contoh generic
# String
name = "Andi"
name1 = "Ujang"
str =  "Hello " + name
format_str = f"Hello {name1}"

print(format_str);

# Boolean
boolean  = False
format_boole = f"boolean: {boolean}"

print(format_boole)

# Angka
angka = 79.47
format_angk = f"angka: {angka}"

print(format_angk)

# Bilangan Bulat 
angka  = 19
format_angk = f"bilangan bulat: {angka:d}"

print(format_angk)

# bilangan ribuan
angka = 10000000
format_angk = f"ribuan: {angka:,}"

print(format_angk)

# bilangan desimal
angka = 795.475323
format_angk = f"desimal: {angka:.3f}"

print(format_angk)

# Leading Zero
angka = 729.35187
format_angk = f"angka: {angka:08.3f}"

print(format_angk)

# Menampilkan tanda + atau -
angka_minus = -93
angka_plus = 84
format_minus = f"Minus: {angka_minus:+d}"
format_plus = f"Plus: {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# Mmeformat persen
persentase = 0.075
format_persen = f"Persen: {persentase:.2%}"

print(format_persen)

# Melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total: {harga*jumlah:,}"
print(format_string)

# Format angka lain (binary, octal, hexadecimal)
angka =  254
format_binary = f"Binary: {bin(angka)}"
format_octal = f"Octal: {oct(angka)}"
format_hexa = f"Hexadecimal: {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexa)

