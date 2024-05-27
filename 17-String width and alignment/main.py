# Width and Multiline

# Data
data_nama = "Budi Cahyadi"
data_umur =  27
data_tinggi = 169.7
data_ukuran_sepatu =  43

#  String
data_string = f"Nama: {data_nama}, Umur: {data_umur}, Tinggi: {data_tinggi}, Ukuran Sepatu: {data_ukuran_sepatu}"
print(10*"=" + " Data String " + 10*"=")
print(data_string)

#  String Multiline (\n)
data_string = f"Nama: {data_nama}, \nUmur: {data_umur}, \nTinggi: {data_tinggi}, \nUkuran Sepatu: {data_ukuran_sepatu}"
print("\n" + 10*"=" + " Data String " + 10*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""Nama  : {data_nama:>2},
Umur  : {data_umur:>2},
Tinggi: {data_tinggi:>2},
Sepatu: {data_ukuran_sepatu:>2}
"""
print("\n" + 10*"=" + " Data String " + 10*"=")
print(data_string)

