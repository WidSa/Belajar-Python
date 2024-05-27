# Tipe Data

# Integer
data1 = 9
print("Data 1 :", data1, ", Bertipe: ", type(data1))

# Float (angka koma)
data2 = 5.7
print("Data 2 :", data2, ", Bertipe: ", type(data2))

# String (kumpulan character)
data3 = "Budi"
print("Data 3 :", data3, ", Bertipe: ", type(data3))

# Boolean (True/False)
data4 = True
print("Data 4 :", data4, ", Bertipe: ", type(data4))

# Tipe Data Khusus
# bilangan kompleks

data_compleks =  complex(7,4)
print("Data 5 :", data_compleks, ", Bertipe: ", type(data_compleks))

# tipe data dari bahasa C

from ctypes import c_double

data_c_double =c_double(15.75)
print("Data 6 :", data_c_double, ", Bertipe: ", type(data_c_double))
