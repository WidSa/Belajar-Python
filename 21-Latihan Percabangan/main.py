# Latihan 

# Calculator Sederhana

print(7*"=" + " Kalkulator Sederhana " + 7*"=")
input_pertama = float(input("Masukan angka pertama: "))
input_kedua = float(input("Masukkan angka kedua: "))
input_Operator = input("Masukkan operator (+, -, x, /): ")

if input_Operator == "+":
    hasil = input_pertama + input_kedua
    print(f"Hasil: {input_pertama} {input_Operator} {input_kedua} = {hasil}")
elif input_Operator == "-":
    hasil = input_pertama - input_kedua
    print(f"Hasil: {input_pertama} {input_Operator} {input_kedua} = {hasil}")
elif input_Operator == "x" or input_Operator == "X" or input_Operator == "*":
    hasil =  input_pertama * input_kedua
    print(f"Hasil: {input_pertama} {input_Operator} {input_kedua} = {hasil}")
elif input_Operator == "/":
    hasil =  input_pertama / input_kedua
    print(f"Hasil: {input_pertama} {input_Operator} {input_kedua} = {hasil}")
else:
    print("Masukkan sesuai yang diminta")
print("Akhir dari program")
