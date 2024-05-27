# Date and Time 
import datetime as dt

# hari_ini = dt.date.today()
# print(f"Hari ini adalaha hari: {hari_ini:%A}")

# tanggal = dt.date(1997, 10, 8)
# print(f"Hari ini adalah hari: {tanggal:%A}")

print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda? \n")
tanggal = int(input("Tanggal\t: "))
bulan = int(input("Bulan\t: "))
tahun = int(input("Tahun\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir: {tanggal_lahir}")
print(f"Harinya Adalah: {tanggal_lahir:%A}")

hari_ini =  dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days//365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Umur andah adalah: {umur_tahun} tahun {umur_bulan_sisa} bulan")
